"""

This is the main file for my Stock Analyzer project. 
It will be used to run the program and call the functions from the functions.py file.

***THIS IS NOT FOR INVESTMENT PURPOSES, USE AT YOUR OWN RISK***

***I AM NOT RESPONSIBLE FOR ANY LOSSES YOU MAY INCUR***

Author: Richard Cook
Created on: 1/20/2023
Last Updated: 1/23/2023

Copyright 2023, all rights reserved.

"""


from functions import adx
from functions import boll
from functions import macd
import pandas as pd
from yahoo_fin import stock_info
from plotly.offline import plot
# from plotly.offline import init_notebook_mode
# init_notebook_mode()
import plotly
import cufflinks as cf
cf.set_config_file(offline=True)
setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


TICKER = "TSLA"
NUM_OF_TICKERS = 100
DI_UPPER = 6  # 10-yr GOOG: 31, 10-yr AAPL: 39, Original: 7
DI_LOWER = 17  # 10-yr GOOG: 32, 10-yr AAPL: 30, Original: 15

global BEST_UPPER
BEST_UPPER = -100
global BEST_LOWER
BEST_LOWER = -100
global BEST_GAIN
BEST_GAIN = 0
global running_investment
running_investment = 0
global full_cost
full_cost = 0
global total_revenue
total_revenue = 0

watchlist_path = "/Users/Cook/Documents/VS Code/Stock Analyzer/Yahoo Ticker Symbols - September 2017.csv"


def get_ticker_symbols():

    tickers = pd.read_csv(watchlist_path)
    ticker_symbols = tickers["Ticker"].iloc[0:NUM_OF_TICKERS]

    return ticker_symbols

# Get the data


def Get_Data(i):
    data = {}
 
    data[i] = stock_info.get_data(
        f"{i}", start_date='01-01-2015',  end_date='12-31-2022')
    

    # data = {}
    # data[i] = stock_info.get_data(
    #     f"{TICKER}", start_date='12-01-2019',  end_date='02-01-2023')
    # print(data['AAPL'].head())
    # print(data["AAPL"])

    # qf = cf.QuantFig(data[i], title=f"{i} Stock Data")
    # # qf.add_bollinger_bands(boll_std=2)
    # qf.add_macd()
    # # # qf.add_rsi()
    # qf.add_dmi()
    # qf.iplot()

    # h= print(data['TSLA'])

    # i = data['Stock']

    j = boll(data[i]['close'], include=False, length=14, fillna=True)
    v = adx(data[i], include=False, length=14, fillna=True)
    w = macd(data[i]['close'], include=False, fillna=True)

    k = pd.concat([data[i], j], axis=1)
    k = pd.concat([k, v], axis=1)
    k = pd.concat([k, w], axis=1)

    # print(type(i))

    # print(type(j))

    # print(k)
    return k


def Boll_Results(k):
    boll_results = pd.DataFrame(
        columns=['Index', 'Close', 'Upper', 'Lower', 'Boll Condition'])
    for index, row in k.iterrows():
        if row['high'] > row['UPPER(close,20)']:
            condition = "Sell"
        elif row['low'] < (row['LOWER(close,20)'] - 0.30*row['LOWER(close,20)']):
            condition = "Buy"
        else:
            condition = "Hold"
        new_row = pd.DataFrame({'Index': index, 'Close': row['close'], 'Upper': row['UPPER(close,20)'],
                                'Lower': row['LOWER(close,20)'], 'Boll Condition': condition}, index=[0])
        boll_results = pd.concat(
            [boll_results, new_row], ignore_index=True)
    return boll_results


def ADX_Results(k):
    adx_results = pd.DataFrame(
        columns=['ADX', 'DI+', 'DI-', 'ADX Condition'])
    for index, row in k.iterrows():
        if row['DI-(14)'] >= 33.33 and row['ADX(14)'] >= row['DI-(14)'] >= row['DI+(14)']:
            condition = "Hold"
        elif  row['DI-(14)'] >= 33.33 or row['ADX(14)'] >= row['DI-(14)'] >= row['DI+(14)'] or row['DI-(14)'] >= row['ADX(14)'] >= row['DI+(14)']:            #elif row['DI-(14)'] > row['DI+(14)'] + DI_LOWER:
            condition = "Buy"
        elif ((((row['DI-(14)']-.1) <= row['ADX(14)'] <= row['DI+(14)']) ) or (((row['ADX(14)'] >= row['DI+(14)']) or row['ADX(14)'] >= row['DI-(14)']) and (row['ADX(14)'] - 15 >= row['DI+(14)']))):     #and (abs(row['DI+(14)'] - row['ADX(14)'])) < 1                             #if row['DI+(14)'] > row['DI-(14)'] + DI_UPPER:
            condition = "Sell"
        else:
            condition = "Hold"
        new_row = pd.DataFrame({'ADX': row['ADX(14)'], 'DI+': row['DI+(14)'], 'DI-': row['DI-(14)'],
                                'ADX Condition': condition, 'Volume': row['volume']}, index=[0])
        adx_results = pd.concat(
            [adx_results, new_row], ignore_index=True)
    return adx_results


def MACD_Results(k):
    macd_results = pd.DataFrame(
        columns=['MACD', 'MACD Signal', 'MACD Condition'])
    delta = [0,0]
    for index, row in k.iterrows():
        delta.append(row['MACD(close,[12,26])'] - row['SIGNAL(close,9)'])
        if row['MACD(close,[12,26])'] < row['SIGNAL(close,9)']:
            condition1 = "Buy"
        elif row['MACD(close,[12,26])'] > row['SIGNAL(close,9)']:
            condition1 = "Sell"
        else:
            condition1 = "Hold"
        try:
            if delta[-1] - delta[-2] > 0:
                    condition2 = "Diverging"
            elif delta[-1] - delta[-2] < 0:
                    condition2 = "Converging"
            else:
                condition2 = "Hold"
        except IndexError:
            pass


        new_row = pd.DataFrame({'MACD': row['MACD(close,[12,26])'], 'MACD Signal': row['SIGNAL(close,9)'],
                                'MACD Condition': condition1, 'MACD Convergence': condition2}, index=[0])
        macd_results = pd.concat(
            [macd_results, new_row], ignore_index=True)
    return macd_results


def Aggr_Results():
    results = pd.concat(
        [Boll_Results(stock_data), ADX_Results(stock_data), MACD_Results(stock_data)], axis=1)
    aggr_results = pd.DataFrame(columns=['Index', 'Close', 'Upper', 'Lower', 'Boll Condition',
                                'ADX', 'DI+', 'DI-', 'ADX Condition', 'Aggr Condition', 'MACD', 'MACD Signal', 'MACD Condition','MACD Convergence', 'Volume'])
    price = []
    for index, row in results.iterrows():
        if row['ADX Condition'] == "Buy":  # row['Boll Condition'] == "Buy" or
            condition = "Buy"
            price.append(row['Close'])
        elif len(price) > 0 and (row['ADX Condition'] == "Sell" and row["Close"] > price[-1]):
            # row['ADX Condition'] == "Sell" and row["Close"] > price[0]:
            condition = "Sell"
            price = []
        else:
            condition = "Hold"

        # if row['ADX Condition'] == "Buy":
        #     condition = "Buy"
        # elif row['ADX Condition'] == "Sell":
        #     condition = "Sell"
        # else:
        #     condition = "Hold"

        # if (row['MACD Condition'] == "Buy" and row['MACD Convergence'] == "Converging") or row['ADX Condition'] == "Buy":
        #     condition = "Buy"
        # elif row['MACD Condition'] == "Buy" and row['MACD Convergence'] == "Diverging":
        #     condition = "Hold"
        # elif row['MACD Condition'] == "Sell" and row['MACD Convergence'] == "Diverging":
        #     condition = "Hold"
        # elif (row['MACD Condition'] == "Sell" and row['MACD Convergence'] == "Converging") or row['ADX Condition'] == "Sell":
        #     condition = "Sell"
        # else:
        #     condition = "Hold"
        

        new_row_aggr = pd.DataFrame({'Index': row['Index'], 'Close': row['Close'], 'Upper': row['Upper'], 'Lower': row['Lower'], 'Boll Condition': row['Boll Condition'],
                                    'ADX': row['ADX'], 'DI+': row['DI+'], 'DI-': row['DI-'], 'ADX Condition': row['ADX Condition'], 'Aggr Condition': condition, 'Volume': row['Volume']}, index=[0])
        aggr_results = pd.concat(
            [aggr_results, new_row_aggr], ignore_index=True)
    return aggr_results


def Analyze_Results():
    aggr_results = Aggr_Results()
    running_revenue = 0
    running_cost = 0
    cycle_number_of_stocks = 0
    cycle_revenue = 0
    global cycle_cost
    cycle_cost = 0
    cycle_count = 0
    total_gain = 0
    total_stocks_bought = 0
    global INITIAL_INVESTMENT
    INITIAL_INVESTMENT = 1000
    is_buying = False
    
    for index, row in aggr_results.iterrows():
        if row['Aggr Condition'] == "Buy" and not is_buying and INITIAL_INVESTMENT > row["Close"]:
            is_buying = True
            cycle_number_of_stocks = 1
            total_stocks_bought += INITIAL_INVESTMENT / row['Close']
            cycle_count += 1
            cycle_cost -= row['Close'] * total_stocks_bought
            running_cost -= row['Close'] * total_stocks_bought
            INITIAL_INVESTMENT -= row['Close'] * total_stocks_bought
            start_date = row['Index']
            print(
                f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}")
            sold = False
        elif is_buying:
            if row['Aggr Condition'] == "Sell":
                is_buying = False
                cycle_revenue = ((total_stocks_bought) * row['Close'])
                INITIAL_INVESTMENT += cycle_revenue
                running_revenue += cycle_revenue

                print(
                    f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}\n")
                cycle_gain = round((cycle_revenue + cycle_cost) /
                                   abs(cycle_cost)*100, 2)
                total_gain += cycle_gain
                stop_date = row['Index']
                cycle_number_of_stocks = 0
                print(
                    f"The lap gain is {cycle_gain} from {start_date} to {stop_date}\nWith a cost of {round(-cycle_cost,2)}\nAnd a revenue of {round(cycle_revenue,2)}\nAnd an investment pool of {INITIAL_INVESTMENT}\n")
                cycle_revenue = 0
                cycle_cost = 0
                total_stocks_bought = 0

            elif INITIAL_INVESTMENT > row["Close"]:
                # cycle_number_of_stocks = 1
                # total_stocks_bought += cycle_number_of_stocks
                # cycle_cost -= row['Close']*cycle_number_of_stocks
                # running_cost -= row['Close']*cycle_number_of_stocks
                # INITIAL_INVESTMENT -= row['Close']*cycle_number_of_stocks
                # if row['Aggr Condition'] == "Buy":
                #     cycle_number_of_stocks = 1
                #     total_stocks_bought += cycle_number_of_stocks
                #     cycle_cost -= row['Close']*cycle_number_of_stocks
                #     running_cost -= row['Close']
                #     INITIAL_INVESTMENT -= row['Close']*cycle_number_of_stocks

                sold = False
                print(
                    f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}")
            else:
                print(
                    f"No stocks purchased at {round(float(row['Close']),2)}")
                pass

    try:
        total_gain = (
            ((running_revenue + (running_cost - cycle_cost))/abs(running_cost))*100)
    except ZeroDivisionError:
        total_gain = 0
    print(
        f"\nTotal Cost to Date (Including Held Positions): {round(-running_cost + cycle_cost,2)}")
    print(
        f"Total Revenue to Date (Excluding Held Positions): {round(running_revenue,2)}")
    print(
        f"Total Gain over Investment Period: {round(total_gain,2)}")
    try:
        print(
            f"Average Full Cycle Gain: {round(total_gain/cycle_count,2)} over {cycle_count} cycles\n")
    except ZeroDivisionError:
        print(f"Average Full Cycle Gain: {round(0,2)}\n")

    actual_gain = ((running_revenue+running_cost)/(-running_cost))*100

    global BEST_GAIN
    if actual_gain > BEST_GAIN:
        BEST_GAIN = actual_gain
        global BEST_UPPER
        BEST_UPPER = DI_UPPER
        global BEST_LOWER
        BEST_LOWER = DI_LOWER
    print(
        f" The best gain {BEST_GAIN}, with a Best Upper of {BEST_UPPER}, and a Best Lower of {BEST_LOWER}")
    global running_investment
    running_investment += INITIAL_INVESTMENT - 100000
    global full_cost
    full_cost += -running_cost
    global total_revenue
    total_revenue += running_revenue
    print(INITIAL_INVESTMENT)
    print(f"running cost is {running_cost}")
    print(f"running revenue is {running_revenue}")
    print((total_revenue))
    print((full_cost))
    print(actual_gain)


symbols = get_ticker_symbols()
STOCKS = []

total_analyzed = 1
for i in symbols:
    ticker = i
    print(ticker)
    stock_data = Get_Data(ticker)
    Analyze_Results()
    print("\n")
    
    if INITIAL_INVESTMENT > 0:
        STOCKS.append([ticker, INITIAL_INVESTMENT])
    if -cycle_cost > 0:
        STOCKS.append([ticker, -cycle_cost])
    melded_profit = 0
    if INITIAL_INVESTMENT > 0:
        melded_profit += INITIAL_INVESTMENT
    if -cycle_cost > 0:
        melded_profit += -cycle_cost
    
    for j in range (0, len(STOCKS)-1):
        melded_profit += STOCKS[j][1]
    melded_profit = melded_profit/total_analyzed


    
    
    total_analyzed += 1

    BEST_GAIN = -100

    print(STOCKS)
    print(melded_profit)
    print(len(STOCKS))