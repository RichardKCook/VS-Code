from __future__ import annotations

import datetime
import threading
import time
import pytz
import pickle

import alpaca_trade_api as tradeapi
import gym
import numpy as np
import pandas as pd
import torch
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split
from finrl.agents.stablebaselines3.models import DRLAgent
from finrl.meta.env_stock_trading.env_stocktrading import StockTradingEnv
from finrl.meta.preprocessor.yahoodownloader import YahooDownloader
from finrl.meta.data_processor import DataProcessor
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split
from finrl import config_tickers
import itertools
from finrl.config import (
    DATA_SAVE_DIR,
    TRAINED_MODEL_DIR,
    TENSORBOARD_LOG_DIR,
    RESULTS_DIR,
    INDICATORS,
    TRAIN_START_DATE,
    TRAIN_END_DATE,
    TEST_START_DATE,
    TEST_END_DATE,
    TRADE_START_DATE,
    TRADE_END_DATE,
)

from finrl.meta.data_processors.processor_alpaca import AlpacaProcessor


class AlpacaPaperTrading:
    def __init__(
        self,
        ticker_list,
        time_interval,
        drl_lib,
        agent,
        cwd,
        state_dim,
        action_dim,
        API_KEY,
        API_SECRET,
        API_BASE_URL,
        tech_indicator_list,
        turbulence_thresh=30,
        max_stock=1e2,
        latency=None,
    ):
        self.model_name = "my_first_model"
        # load agent
        self.drl_lib = drl_lib
        if agent == "ppo":
            if drl_lib == "elegantrl":
                from elegantrl.agents import AgentPPO
                # from elegantrl.train.run import init_agent
                # from elegantrl.train.config import (
                #     Arguments,
                # )  # bug fix:ModuleNotFoundError: No module named 'elegantrl.run'

                # load agent
                config = {
                    "state_dim": state_dim,
                    "action_dim": action_dim,
                }
                # args = Arguments(agent_class=AgentPPO, env=StockEnvEmpty(config))
                # args.cwd = cwd
                # args.net_dim = net_dim
                # load agent
                try:
                    # agent = init_agent(args, gpu_id=0)
                    # self.act = agent.act
                    # self.device = agent.device
                    pass
                except BaseException:
                    raise ValueError("Fail to load agent!")

            elif drl_lib == "rllib":
                from ray.rllib.agents import ppo
                from ray.rllib.agents.ppo import PPOTrainer

                config = ppo.DEFAULT_CONFIG.copy()
                config["env"] = StockEnvEmpty
                config["log_level"] = "WARN"
                config["env_config"] = {
                    "state_dim": state_dim,
                    "action_dim": action_dim,
                }
                trainer = PPOTrainer(env=StockEnvEmpty, config=config)
                trainer.restore(cwd)
                try:
                    trainer.restore(cwd)
                    self.agent = trainer
                    print("Restoring from checkpoint path", cwd)
                except:
                    raise ValueError("Fail to load agent!")

            elif drl_lib == "stable_baselines3":
                from stable_baselines3 import PPO

                try:
                    # load agent
                    self.model = PPO.load("/Users/Cook/Documents/VS Code/FinRC/results/trained_model_20230224-10h54.zip")
                    print("Successfully load model", cwd)
                except:
                    raise ValueError("Fail to load agent!")

            else:
                raise ValueError(
                    "The DRL library input is NOT supported yet. Please check your input."
               )
            
        
        elif agent == "sac":
            if drl_lib == "stable_baselines3":
                from stable_baselines3 import SAC

                try:
                    # load agent
                    self.model = SAC.load("/Users/Cook/Documents/VS Code/FinRC/results/trained_model_20230227-16h14.zip")
                    print("Successfully load SAC model", cwd)
                except:
                    raise ValueError("Fail to load agent!")
    
            else:
                raise ValueError(
                    "The DRL library input is NOT supported yet. Please check your input."
                )
            
        else:
            raise ValueError("Agent input is NOT supported yet.")

        # connect to Alpaca trading API
        try:
            self.alpaca = tradeapi.REST(API_KEY, API_SECRET, API_BASE_URL, api_version="v2")
        except:
            raise ValueError(
                "Fail to connect Alpaca. Please check account info and internet connection."
            )

        # read trading time interval
        if time_interval == "1s":
            self.time_interval = 1
        elif time_interval == "5s":
            self.time_interval = 5
        elif time_interval == "1Min":
            self.time_interval = 60
        elif time_interval == "5Min":
            self.time_interval = 60 * 5
        elif time_interval == "15Min":
            self.time_interval = 60 * 15
        elif (
            time_interval == "1D" or time_interval == "1d"
        ):  # bug fix:1D ValueError: Time interval input is NOT supported yet. Maybe any other better ways
            self.time_interval = 15 * 60 * 60
        else:
            raise ValueError("Time interval input is NOT supported yet.")

        # read trading settings
        self.tech_indicator_list = tech_indicator_list
        self.turbulence_thresh = turbulence_thresh
        self.max_stock = max_stock

        # initialize account
        self.stocks = np.asarray([0] * len(ticker_list))  # stocks holding
        self.stocks_cd = np.zeros_like(self.stocks)
        self.cash = float(self.alpaca.get_account().cash)  # cash record
        self.stocks_df = pd.DataFrame(
            self.stocks, columns=["stocks"], index=ticker_list
        )
        self.asset_list = []
        self.price = np.asarray([0] * len(ticker_list))
        self.stockUniverse = ticker_list
        self.turbulence_bool = 0
        self.equities = []
       
    

    def test_latency(self, test_times=10):
        total_time = 0
        for i in range(0, test_times):
            time0 = time.time()
            self.get_state()
            time1 = time.time()
            temp_time = time1 - time0
            total_time += temp_time
        latency = total_time / test_times
        print("latency for data processing: ", latency)
        return latency

    def run(self):
        print(self.alpaca.get_account())
        orders = self.alpaca.list_orders(status="open")
        for order in orders:
            self.alpaca.cancel_order(order.id)

        # Wait for market to open.
        print("Waiting for market to open...")
        tAMO = threading.Thread(target=self.awaitMarketOpen)
        tAMO.start()
        tAMO.join()
        print("Market opened.")
        while True:
            # # Figure out when the market will close so we can prepare to sell beforehand.
            # clock = self.alpaca.get_clock()
            # closingTime = clock.next_close.replace(
            #     tzinfo=datetime.timezone.utc
            # ).timestamp()
            # currTime = clock.timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()
            # self.timeToClose = closingTime - currTime

            # if self.timeToClose < (15):
            #     # Close all positions when 1 minutes til market close.
            #     # print("Market closing soon. Stop trading.")
                

            # #     """# Close all positions when 1 minutes til market close.
            # # print("Market closing soon.  Closing positions.")

            # # positions = self.alpaca.list_positions()
            # # for position in positions:
            # #   if(position.side == 'long'):
            # #     orderSide = 'sell'
            # #   else:
            # #     orderSide = 'buy'
            # #   qty = abs(int(float(position.qty)))
            # #   respSO = []
            # #   tSubmitOrder = threading.Thread(target=self.submitOrder(qty, position.symbol, orderSide, respSO))
            # #   tSubmitOrder.start()
            # #   tSubmitOrder.join()

            # # Run script again after market close for next trading day.
            #     print("Sleeping until market close (15 minutes).")
            #     time.sleep(60 * 15)
            

            # else:
                trade = threading.Thread(target=self.trade)
                trade.start()
                trade.join()
                last_equity = float(self.alpaca.get_account().last_equity)
                cur_time = time.time()
                self.equities.append([cur_time, last_equity])
                time.sleep(self.time_interval)
                self.awaitMarketOpen()
                
                
    
    def awaitMarketOpen(self):
        import pandas_market_calendars as mcal

        eastern = pytz.timezone('US/Eastern')
        isOpen = False
        while not isOpen:
            nyse = mcal.get_calendar('NYSE')
            schedule = nyse.schedule(start_date=datetime.datetime.now(), end_date=datetime.datetime.now())
            is_trading_day = len(schedule) != 0
            now = datetime.datetime.now(eastern)
            if is_trading_day and now.time() >= datetime.time(9, 45) and now.time() <= datetime.time(16, 0):
                isOpen = True 
            else:
                print("Waiting for market to open...")
                time.sleep(60)

    def trade(self):
        state = self.get_state()

        if self.drl_lib == "elegantrl":
            with torch.no_grad():
                s_tensor = torch.as_tensor((state,), device=self.device)
                a_tensor = self.act(s_tensor)
                action = a_tensor.detach().cpu().numpy()[0]

            action = (action * self.max_stock).astype(int)

        elif self.drl_lib == "rllib":
            action = self.agent.compute_single_action(state)

        elif self.drl_lib == "stable_baselines3":
            # action = self.model.predict(state)[0]

            stock_dimension = len(state.tic.unique())
            state_space = 1 + 2*stock_dimension + len(INDICATORS)*stock_dimension
            buy_cost_list = sell_cost_list = [0.001] * stock_dimension
            num_stock_shares = [0] * stock_dimension
            env_kwargs = {
                            "hmax": 50,
                            "initial_amount": 100000,
                            "num_stock_shares": num_stock_shares,
                            "buy_cost_pct": buy_cost_list,
                            "sell_cost_pct": sell_cost_list,
                            "state_space": state_space,
                            "stock_dim": stock_dimension,
                            "tech_indicator_list": INDICATORS,
                            "action_space": stock_dimension,
                            "reward_scaling": 1e-4
                        }
            try:
                previous_state = []
                initial_tf = True
                # with open('e_trade_gym.pickle', 'rb') as f:
                #     previous_state = pickle.load(f)
                #     initial_tf = False
            except FileNotFoundError:
                previous_state = []
                initial_tf = True
            
            e_trade_gym = StockTradingEnv(df = state, previous_state= previous_state,turbulence_threshold = 70,risk_indicator_col='vix', **env_kwargs, initial = initial_tf)
            # save the environment to a file
            last_state = e_trade_gym.render()
            df_last_state = pd.DataFrame({"last_state": last_state})
            df_last_state.to_csv(f"last_state__{datetime.datetime.now()}.csv", index=False)
            with open('e_trade_gym.pickle', 'wb') as f:
                pickle.dump(last_state, f)
            df_account_value, action= DRLAgent.DRL_prediction(
                    model=self.model,
                    environment = e_trade_gym)
            
            action.index = pd.to_datetime(action.index) + pd.Timedelta(days=1)
            print(action)

        else:
            raise ValueError(
                "The DRL library input is NOT supported yet. Please check your input."
            )

        self.stocks_cd += 1
        if self.turbulence_bool == 0:
            min_action = 0  # stock_cd
            last_row = action.tail(1)
            print(last_row)
            for col in last_row:
                column = self.stockUniverse.index(col)
                trades = last_row[col].values[0]
                if trades < -min_action:
                    sell_num_shares = min(self.stocks[column], -trades)
                    qty = abs(int(sell_num_shares))
                    respSO = []
                    tSubmitOrder = threading.Thread(
                        target=self.submitOrder(qty, self.stockUniverse[column], "sell", respSO)
                    )
                    tSubmitOrder.start()
                    tSubmitOrder.join()
                    self.cash = float(self.alpaca.get_account().cash)
                    self.stocks_cd[column] = 0
                elif trades > min_action:
                    if self.cash < 0:
                        tmp_cash = 0
                    else:
                        tmp_cash = self.cash
                    buy_num_shares = min(
                        tmp_cash // self.price[column], abs(int(trades))
                    )
                    qty = abs(int(buy_num_shares))
                    respSO = []
                    tSubmitOrder = threading.Thread(
                        target=self.submitOrder(qty, self.stockUniverse[column], "buy", respSO)
                    )
                    tSubmitOrder.start()
                    tSubmitOrder.join()
                    self.cash = float(self.alpaca.get_account().cash)
                    self.stocks_cd[column] = 0

        else:  # sell all when turbulence
            positions = self.alpaca.list_positions()
            for position in positions:
                if position.side == "long":
                    orderSide = "sell"
                else:
                    orderSide = "buy"
                qty = abs(int(float(position.qty)))
                respSO = []
                tSubmitOrder = threading.Thread(
                    target=self.submitOrder(qty, position.symbol, orderSide, respSO)
                )
                tSubmitOrder.start()
                tSubmitOrder.join()

            self.stocks_cd[:] = 0

    def get_state(self):
        TRADE_START_DATE = '2023-02-24' #must be the trading day before the most recent trading day when you start
        TRADE_START_DATE = datetime.datetime.strptime(TRADE_START_DATE, '%Y-%m-%d').date()

        TRAIN_START_DATE = "2001-01-01"
        TRAIN_END_DATE = TRADE_START_DATE
        TRADE_END_DATE = datetime.date.today() + datetime.timedelta(days=1)
        TRADE_START_DATE = str(TRADE_START_DATE)
        TRADE_END_DATE = str(TRADE_END_DATE)
        TRAIN_START_DATE = str(TRAIN_START_DATE)
        TRAIN_END_DATE = str(TRAIN_END_DATE)
        df = YahooDownloader(start_date = TRAIN_START_DATE,
                     end_date = TRADE_END_DATE,
                     ticker_list = config_tickers.DOW_30_TICKER).fetch_data()
        df.sort_values(['date','tic'],ignore_index=True)
        
        fe = FeatureEngineer(
                    use_technical_indicator=True,
                    tech_indicator_list = INDICATORS,
                    use_vix=True,
                    use_turbulence=True,
                    user_defined_feature = False)

        processed = fe.preprocess_data(df)
        
        list_ticker = processed["tic"].unique().tolist()
        list_date = list(pd.date_range(processed['date'].min(),processed['date'].max()).astype(str))
        combination = list(itertools.product(list_date,list_ticker))

        processed_full = pd.DataFrame(combination,columns=["date","tic"]).merge(processed,on=["date","tic"],how="left")
        processed_full = processed_full[processed_full['date'].isin(processed['date'])]
        processed_full = processed_full.sort_values(['date','tic'])

        processed_full = processed_full.fillna(0)
        train = data_split(processed_full, TRAIN_START_DATE,TRAIN_END_DATE)
        trade = data_split(processed_full, TRADE_START_DATE,TRADE_END_DATE)

        state = trade


        return state

    def submitOrder(self, qty, stock, side, resp):
        if qty > 0:

            try:
                self.alpaca.submit_order(stock, qty, side, "market", time_in_force="gtc")
                print(
                    "Market order of | "
                    + str(qty)
                    + " "
                    + stock
                    + " "
                    + side
                    + " | completed."
                )
                resp.append(True)
            except:
                print(
                    "Order of | "
                    + str(qty)
                    + " "
                    + stock
                    + " "
                    + side
                    + " | did not go through."
                )
                resp.append(False)
        else:
            print(
                "Quantity is 0, order of | "
                + str(qty)
                + " "
                + stock
                + " "
                + side
                + " | not completed."
            )
            resp.append(True)

    @staticmethod
    def sigmoid_sign(ary, thresh):
        def sigmoid(x):
            return 1 / (1 + np.exp(-x * np.e)) - 0.5

        return sigmoid(ary / thresh) * thresh


class StockEnvEmpty(gym.Env):
    # Empty Env used for loading rllib agent
    def __init__(self, config):
        state_dim = config["state_dim"]
        action_dim = config["action_dim"]
        self.env_num = 1
        self.max_step = 10000
        self.env_name = "StockEnvEmpty"
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.if_discrete = False
        self.target_return = 9999
        self.observation_space = gym.spaces.Box(
            low=-3000, high=3000, shape=(state_dim,333), dtype=np.float32
        )
        self.action_space = gym.spaces.Box(
            low=-1, high=1, shape=(action_dim,333), dtype=np.float32
        )

    def reset(self):
        return

    def step(self, actions):
        return


