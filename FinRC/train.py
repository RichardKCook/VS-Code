import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import datetime
from finrl.config import ALPACA_API_BASE_URL
from finrl.config import ALPACA_API_KEY
from finrl.config import ALPACA_API_SECRET
from finrl.config import DATA_SAVE_DIR
from finrl.config import ERL_PARAMS
from finrl.config import INDICATORS
from finrl.config import RESULTS_DIR
from finrl.config import RLlib_PARAMS
from finrl.config import SAC_PARAMS
from finrl.config import TENSORBOARD_LOG_DIR
# from finrl.config import TEST_END_DATE
# from finrl.config import TEST_START_DATE
# from finrl.config import TRADE_END_DATE
# from finrl.config import TRADE_START_DATE
# from finrl.config import TRAIN_END_DATE
# from finrl.config import TRAIN_START_DATE
from finrl.config import TRAINED_MODEL_DIR
from finrl.config_tickers import DOW_30_TICKER

TRADE_START_DATE = '2023-02-24'
TRADE_START_DATE = datetime.datetime.strptime(TRADE_START_DATE, '%Y-%m-%d').date()

TRAIN_START_DATE = "2001-01-01"
TRAIN_END_DATE = TRADE_START_DATE
TRADE_END_DATE = datetime.date.today() + datetime.timedelta(days=1)
TRADE_START_DATE = str(TRADE_START_DATE)
TRADE_END_DATE = str(TRADE_END_DATE)
TRAIN_START_DATE = str(TRAIN_START_DATE)
TRAIN_END_DATE = str(TRAIN_END_DATE)

# %matplotlib inline
from finrl.meta.preprocessor.yahoodownloader import YahooDownloader
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split
from finrl.meta.env_stock_trading.env_stocktrading import StockTradingEnv
from finrl.agents.stablebaselines3.models import DRLAgent
from stable_baselines3.common.logger import configure
from finrl.meta.data_processor import DataProcessor

from finrl.plot import backtest_stats, backtest_plot, get_daily_return, get_baseline

from pprint import pprint

import sys
sys.path.append("../FinRC")
import alpaca_trade_api as tradeapi

import itertools


def train(start_date,
            end_date,
            ticker_list,
            data_source,
            time_interval,
            technical_indicator_list,
            drl_lib,
            env,
            model_name,
            cwd,
            erl_params,
            rllib_params,
            break_step,
            kwargs
        ):
    

    df = YahooDownloader(TRAIN_START_DATE,
                     TRADE_END_DATE,
                     ticker_list).fetch_data()
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

    processed_full.sort_values(['date','tic'],ignore_index=True)

    


    train = data_split(processed_full, TRAIN_START_DATE,TRAIN_END_DATE)
    trade = data_split(processed_full, TRADE_START_DATE,TRADE_END_DATE)
    print(len(train))
    print(len(trade))

    stock_dimension = len(train.tic.unique())
    state_space = 1 + 2*stock_dimension + len(INDICATORS)*stock_dimension
    print(f"Stock Dimension: {stock_dimension}, State Space: {state_space}")

    buy_cost_list = sell_cost_list = [0.001] * stock_dimension
    num_stock_shares = [0] * stock_dimension

    env_kwargs = {
        "hmax": 100,
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



    e_train_gym = StockTradingEnv(df = train, **env_kwargs)

    env_train, _ = e_train_gym.get_sb_env()
    print(type(env_train))

    agent = DRLAgent(env = env_train)
    
    if_using_a2c = False
    if_using_ddpg = False
    if_using_ppo = False
    if_using_td3 = False
    if_using_sac = True

#     model_a2c = agent.get_model("a2c")

#     if if_using_a2c:
#         # set up logger
#         tmp_path = RESULTS_DIR + '/a2c'
#         new_logger_a2c = configure(tmp_path, ["stdout", "csv", "tensorboard"])
#         # Set new logger
#         model_a2c.set_logger(new_logger_a2c)

#     trained_a2c = agent.train_model(model=model_a2c, 
#                              tb_log_name='a2c',
#                              total_timesteps=50000) if if_using_a2c else None
    
#     model_ddpg = agent.get_model("ddpg")

#     if if_using_ddpg:
#         # set up logger
#         tmp_path = RESULTS_DIR + '/ddpg'
#         new_logger_ddpg = configure(tmp_path, ["stdout", "csv", "tensorboard"])
#         # Set new logger
#         model_ddpg.set_logger(new_logger_ddpg)

#     trained_ddpg = agent.train_model(model=model_ddpg, 
#                              tb_log_name='ddpg',
#                              total_timesteps=50000) if if_using_ddpg else None
    
#     PPO_PARAMS = {
#     "n_steps": 2048,
#     "ent_coef": 0.01,
#     "learning_rate": 0.00025,
#     "batch_size": 128,
# }
#     model_ppo = agent.get_model("ppo",model_kwargs = PPO_PARAMS)

#     if if_using_ppo:
#         # set up logger
#         tmp_path = RESULTS_DIR + '/ppo'
#         new_logger_ppo = configure(tmp_path, ["stdout", "csv", "tensorboard"])
#         # Set new logger
#         model_ppo.set_logger(new_logger_ppo)

#     trained_ppo = agent.train_model(model=model_ppo, 
#                              tb_log_name='ppo',
#                              total_timesteps=50000) if if_using_ppo else None
    

#     TD3_PARAMS = {"batch_size": 100, 
#               "buffer_size": 1000000, 
#               "learning_rate": 0.001}

#     model_td3 = agent.get_model("td3",model_kwargs = TD3_PARAMS)

#     if if_using_td3:
#         # set up logger
#         tmp_path = RESULTS_DIR + '/td3'
#         new_logger_td3 = configure(tmp_path, ["stdout", "csv", "tensorboard"])
#         # Set new logger
#         model_td3.set_logger(new_logger_td3)

#     trained_td3 = agent.train_model(model=model_td3, 
#                              tb_log_name='td3',
#                              total_timesteps=30000) if if_using_td3 else None
    
    SAC_PARAMS = {
    "batch_size": 256,
    "buffer_size": 100000,
    "learning_rate": 0.009846738873614562,
    "learning_starts": 1000,
    "ent_coef": 0.01, #"auto_0.1"
}

    model_sac = agent.get_model("sac",model_kwargs = SAC_PARAMS)

    if if_using_sac:
        # set up logger
        tmp_path = RESULTS_DIR + '/sac'
        new_logger_sac = configure(tmp_path, ["stdout", "csv", "tensorboard"])
        # Set new logger
        model_sac.set_logger(new_logger_sac)

    trained_sac = agent.train_model(model=model_sac, 
                            tb_log_name='sac',
                            total_timesteps=40000) if if_using_sac else None
        
    data_risk_indicator = processed_full[(processed_full.date<TRAIN_END_DATE) & (processed_full.date>=TRAIN_START_DATE)]
    insample_risk_indicator = data_risk_indicator.drop_duplicates(subset=['date'])

    insample_risk_indicator.vix.describe()

    print(trade)

    e_trade_gym = StockTradingEnv(df = trade, turbulence_threshold = 70,risk_indicator_col='vix', **env_kwargs)
    # env_trade, obs_trade = e_trade_gym.get_sb_env()

    trained_moedl = trained_sac
    df_account_value, df_actions = DRLAgent.DRL_prediction(
    model=trained_moedl, 
    environment = e_trade_gym)

    print("==============Get Backtest Results===========")
    now = datetime.datetime.now().strftime('%Y%m%d-%Hh%M')

    perf_stats_all = backtest_stats(account_value=df_account_value)
    perf_stats_all = pd.DataFrame(perf_stats_all)
    perf_stats_all.to_csv("./"+RESULTS_DIR+"/perf_stats_all_"+now+'.csv')

    #baseline stats
    print("==============Get Baseline Stats===========")
    baseline_df = get_baseline(
            ticker="^DJI", 
            start = df_account_value.loc[0,'date'],
            end = df_account_value.loc[len(df_account_value)-1,'date'])

    stats = backtest_stats(baseline_df, value_col_name = 'close')

    print("==============Compare to DJIA===========")
    # %matplotlib inline
    # S&P 500: ^GSPC
    # Dow Jones Index: ^DJI
    # NASDAQ 100: ^NDX
    # backtest_plot(df_account_value, 
    #             baseline_ticker = '^DJI', 
    #             baseline_start = df_account_value.loc[0,'date'],
    #             baseline_end = df_account_value.loc[len(df_account_value)-1,'date'])
    


    save = input("Would you like to save this model? (y/n)").lower()
    if save == 'y':
        trained_moedl.save("./"+RESULTS_DIR+"/trained_model_"+now)
        print("Model saved")
    else:
        print("Model not saved")