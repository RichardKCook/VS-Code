from __future__ import annotations

import random
import time
from copy import deepcopy
import logging
import cloudpickle

import gym
import matplotlib
import numpy as np
import pandas as pd
from gym import spaces
from stable_baselines3.common import logger
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.vec_env import SubprocVecEnv
import numpy as np
import pandas as pd
import gym
from gym import spaces
from gym.utils import seeding
# from gym.envs.classic_control import rendering
from copy import deepcopy



matplotlib.use("Agg")




# StockTradingEnv with StopLoss
class StockTradingEnvStopLoss(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(
        self,
        df,
        ticker_list,
        date_list,
        buy_cost_pct=0.001,
        sell_cost_pct=0.001,
        hmax=10,
        initial_amount=1000000,
        state_space=9,
        stock_dim=None,
        tech_indicator_list=None,
        reward_scaling=1e-4,
        turbulence_threshold=None,
        shares_increment=1,
        output_format='dictionary',
        print_verbosity=10,
        patient=False,
        stoploss_penalty=0.2,
    ):
        self.stock_dim = len(ticker_list)
        self.ticker_list = ticker_list
        self.buy_cost_pct = buy_cost_pct
        self.sell_cost_pct = sell_cost_pct
        self.hmax = hmax
        self.initial_amount = initial_amount
        self.state_space = state_space
        self.reward_scaling = reward_scaling
        self.tech_indicator_list = technical_indicator_list
        self.print_verbosity = print_verbosity
        self.shares_increment = shares_increment
        self.output_format = output_format
        self.patient = patient
        self.stoploss_penalty = stoploss_penalty
        self.turbulence_threshold = turbulence_threshold
        

        self.date_list = date_list
        self.date_index = 0
        self.dates = date_list
        self.stock_data_dict = {}
        self.current_step = 0
        self.trade_data = None
        self.stock_price_history = None
        self.stock_weights = np.zeros((self.stock_dim,))
        self.sum_trades = 0
        self.printed_header = False
        self.n_buy = 0
        self.n_sell = 0
        self.episode = 0
        self.render_on = False
        self.turbulence = 0
        self.avg_buy_price = 0
        self.profit_sell_diff_avg_buy = 0
        self.closing_diff_avg_buy = 0
        self.n_buys = np.zeros((self.stock_dim,))
        self.buy_date_index = np.zeros((self.stock_dim,))
        self.state_memory = []
        self.action_memory = []
        self.reward_memory = []
        self.transaction_memory = []
        self.actions_memory = []
        self.account_information = {"cash": [], "asset_value": [], "total_assets": [], "reward": []}
        self.allowed_reasons = ["update", "STOP LOSS", "LOW PROFIT", "HIGH PROFIT", "CASH SHORTAGE", "TURBULENCE"]
        self.colnames = df.columns.tolist()
        self.stock_data = df.to_dict("list")
        # initialize the logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        # Extract assets and dates from the DataFrame
        self.assets = list(df["tic"].unique())
        self.dates = list(df["date"].unique())
        self.df = df
        self.stock_dimension = len(self.assets)

        self.action_space = spaces.Box(low=-1, high=1, shape=(self.stock_dim,))
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(self.state_space * self.stock_dim + self.stock_dim + 1,))

        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def get_date_vector(self, date, cols=None):
        if cols is None:
            cols = ["date", "open", "high", "low", "close", "volume"]

        res = []
        for col in cols:
            ix = self.colnames.index(col)
            res.append(self.stock_data[ix][date])
        return res

    def log_header(self):
        self.logger.info(
            " | ".join(
                [
                    "step",
                    "tot_reward",
                    "cash",
                    "asset_value",
                    "total_assets",
                    "max_actions",
                    "num_trades",
                ]
            )
        )
        self.printed_header = True

    def log_step(self, reason):
        assert reason in self.allowed_reasons
        state = self.state_memory[-1]
        cash = state[0]
        asset_value = np.dot(state[1 : len(self.assets) + 1], self.get_date_vector(self.date_index, cols=["close"]))
        tot_assets = cash + asset_value
        self.logger.info(
            " | ".join(
                [
                    str(self.current_step),
                    "%.4e" % self.last_total_assets,
                    "%.2f" % cash,
                    "%.2f" % asset_value,
                    "%.4e" % tot_assets,
                    "%.4e" % self.sum_trades,
                    str(self.actual_num_trades),
                ]
            )
            + " | "
            + reason,
        )
        self.last_total_assets = tot_assets

    def get_reward(self):
        # current value
        current_value = self.state_memory[-1][0] + np.dot(self.state_memory[-1][1:], self.get_date_vector(self.date_index, cols=["close"]))
        # previous value
        prev_value = self.state_memory[-2][0] + np.dot(self.state_memory[-2][1:], self.get_date_vector(self.date_index - 1, cols=["close"]))
        # reward is the increase in portfolio value
        reward = (current_value - prev_value) / prev_value
        # scale the reward
        reward = reward * self.reward_scaling
        return reward

    def return_terminal(self, reason):
        state = self.state_memory[-1]
        reward = self.get_reward()
        self.log_step(reason=reason)
        return state, reward, True, {}

    def reset(self):
        self.sum_trades = 0
        self.current_step = 0
        self.printed_header = False
        self.last_total_assets = self.initial_amount
        self.actual_num_trades = 0
        self.account_information = {"cash": [], "asset_value": [], "total_assets": [], "reward": []}
        self.actions_memory = []
        self.transaction_memory = []
        self.state_memory = []
        self.rewards_memory = []
        self.n_buys = np.zeros((self.stock_dim,))
        self.avg_buy_price = np.zeros((self.stock_dim,))
        self.closing_diff_avg_buy = np.zeros((self.stock_dim,))
        self.profit_sell_diff_avg_buy = np.zeros((self.stock_dim,))

        if self.current_prices is None:
            self.current_prices = np.array(
                self.get_date_vector(self.date_index, cols=["close"])
            )

        self.state_memory.append(
            [self.initial_amount]
            + [0] * self.stock_dim
            + self.get_date_vector(self.date_index)
        )
        return self.state_memory[-1]

    def render(self, mode="human"):
        return self.account_information

    def save(self, filename):
        with open(filename, "wb") as fp:
            cloudpickle.dump(self, fp)

    @staticmethod
    def load(filename):
        with open(filename, "rb") as fp:
            obj = cloudpickle.load(fp)
        return obj