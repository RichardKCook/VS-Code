from __future__ import annotations

import os
from argparse import ArgumentParser
from typing import List

from finrl.config import ALPACA_API_BASE_URL
from finrl.config import DATA_SAVE_DIR
from finrl.config import ERL_PARAMS
from finrl.config import INDICATORS
from finrl.config import RESULTS_DIR
from finrl.config import RLlib_PARAMS
from finrl.config import SAC_PARAMS
from finrl.config import TENSORBOARD_LOG_DIR
from finrl.config import TEST_END_DATE
from finrl.config import TEST_START_DATE
from finrl.config import TRADE_END_DATE
from finrl.config import TRADE_START_DATE
# from finrl.config import TRAIN_END_DATE
# from finrl.config import TRAIN_START_DATE
from finrl.config import TRAINED_MODEL_DIR
from finrl.main import check_and_make_directories
check_and_make_directories([DATA_SAVE_DIR, TRAINED_MODEL_DIR, TENSORBOARD_LOG_DIR, RESULTS_DIR])
from finrl.config import INDICATORS
from finrl.config_private import ALPACA_API_KEY, ALPACA_API_SECRET

TRAIN_START_DATE = '2009-01-01'
TRAIN_END_DATE = '2020-07-01'


from finrl.config_tickers import DOW_30_TICKER, NAS_100_TICKER
from finrl.meta.env_stock_trading.env_stocktrading_np import StockTradingEnv

# construct environment

# try:
#     from finrl.config_private import ALPACA_API_KEY, ALPACA_API_SECRET
# except ImportError:
#     raise FileNotFoundError(
#         "Please set your own ALPACA_API_KEY and ALPACA_API_SECRET in config_private.py"
#     )


def build_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--mode",
        dest="mode",
        help="start mode, train, download_data" " backtest",
        metavar="MODE",
        default="trade",
    )
    return parser


# "./" will be added in front of each directory
def check_and_make_directories(directories: list[str]):
    for directory in directories:
        if not os.path.exists("./" + directory):
            os.makedirs("./" + directory)


def main() -> int:
    parser = build_parser()
    options = parser.parse_args()
    check_and_make_directories(
        [DATA_SAVE_DIR, TRAINED_MODEL_DIR, TENSORBOARD_LOG_DIR, RESULTS_DIR]
    )

    if options.mode == "train":
        from train import train

        env = StockTradingEnv

        # demo for elegantrl
        kwargs = (
            {}
        )  # in current meta, with respect yahoofinance, kwargs is {}. For other data sources, such as joinquant, kwargs is not empty
        train(
            start_date=TRAIN_START_DATE,
            end_date=TRAIN_END_DATE,
            ticker_list=DOW_30_TICKER,
            data_source="yahoofinance",
            time_interval="1D",
            technical_indicator_list=INDICATORS,
            drl_lib="stable_baselines3",
            env=env,
            model_name="sac",
            cwd="./test_ppo",
            erl_params=ERL_PARAMS,
            rllib_params=RLlib_PARAMS,
            break_step=1e5,
            kwargs=kwargs,
        )
    elif options.mode == "test":
        from finrl import test

        env = StockTradingEnv

        # demo for elegantrl
        # in current meta, with respect yahoofinance, kwargs is {}. For other data sources, such as joinquant, kwargs is not empty
        kwargs = {}

        account_value_erl = test(  # noqa
            start_date=TEST_START_DATE,
            end_date=TEST_END_DATE,
            ticker_list=DOW_30_TICKER,
            data_source="yahoofinance",
            time_interval="1D",
            technical_indicator_list=INDICATORS,
            drl_lib="elegantrl",
            env=env,
            model_name="ppo",
            cwd="./test_ppo",
            net_dimension=512,
            # kwargs=kwargs,
        )
    elif options.mode == "trade":
        import trade

        try:
            from finrl.config_private import ALPACA_API_KEY, ALPACA_API_SECRET
        except ImportError:
            raise FileNotFoundError(
                "Please set your own ALPACA_API_KEY and ALPACA_API_SECRET in config_private.py"
            )
        env = StockTradingEnv

        universe = trade.AlpacaPaperTrading(
            ticker_list = DOW_30_TICKER,
            time_interval = "1D",
            drl_lib = "stable_baselines3",
            agent = "sac",
            cwd = "/Users/Cook/Documents/VS Code/FinRC/results",
            API_KEY = ALPACA_API_KEY,
            API_SECRET = ALPACA_API_SECRET,
            API_BASE_URL = "https://paper-api.alpaca.markets",
            tech_indicator_list = INDICATORS,
            turbulence_thresh=30,
            max_stock=1e2,
            latency=None,
            state_dim=len(DOW_30_TICKER)  * (len(INDICATORS) + 3)
            + 3,  # bug fix: for ppo add dimension of state/observations space =  len(stocks)* len(INDICATORS) + 3+ 3*len(stocks)
            action_dim=len(
                DOW_30_TICKER
            ),  # bug fix: for ppo add dimension of action space = len(stocks)
        )

        universe.run()

    else:
        raise ValueError("Wrong mode.")
    return 0


# Users can input the following command in terminal
# python main.py --mode=train
# python main.py --mode=test
# python main.py --mode=trade
if __name__ == "__main__":
    raise SystemExit(main())
