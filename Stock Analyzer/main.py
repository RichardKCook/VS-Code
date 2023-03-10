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
import pandas as pd
from yahoo_fin import stock_info
from plotly.offline import plot
# from plotly.offline import init_notebook_mode
# init_notebook_mode()
import plotly
import cufflinks as cf
cf.set_config_file(offline=True)
setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)
from datetime import datetime, timedelta
from time import sleep


TICKER = "AAPL"
NUM_OF_TICKERS = 1

global FULL_SET
FULL_SET = []
global BEST_UPPER_ACTUAL
BEST_UPPER_ACTUAL = -100
global BEST_LOWER_ACTUAL
BEST_LOWER_ACTUAL = -100
global BEST_GAIN
BEST_GAIN = 0
global BEST_CYCLE_GAIN
BEST_CYCLE_GAIN = 0
global BEST_UPPER_CYCLE
BEST_UPPER_ACTUAL = -100
global BEST_LOWER_CYCLE
BEST_LOWER_ACTUAL = -100


global k
k = 0



watchlist_path = "/Users/Cook/Documents/VS Code/Stock Analyzer/Yahoo Ticker Symbols - September 2017.csv"

def get_ticker_symbols():

    tickers = pd.read_csv(watchlist_path)
    ticker_symbols = tickers["Ticker"].iloc[0:NUM_OF_TICKERS]

    return ticker_symbols

# Get the data

def Get_Data(i,date_index):
    data = {}

    # data[i] = stock_info.get_data(
    #     f"{i}", start_date='01-01-2012',  end_date='01-01-2023')

    try:
        data[i] = stock_info.get_data(f"{TICKER}", start_date=(datetime.now() - timedelta(days=365*0.5) + timedelta(days=date_index)), end_date=(datetime.now() + timedelta(date_index)))
    except:
        sleep(600)
        data[i] = stock_info.get_data(f"{TICKER}", start_date=(datetime.now() - timedelta(days=365*0.5) + timedelta(days=date_index)), end_date=(datetime.now() + timedelta(date_index)))
    
    # print(data['AAPL'].head())
    # print(data["AAPL"])

    # qf = cf.QuantFig(data[i], title=f"{i} Stock Data")
    # qf.add_bollinger_bands(boll_std=2)
    # qf.add_macd()
    # qf.add_rsi()
    # qf.add_dmi()
    # qf.iplot()

    # h= print(data['TSLA'])

    # i = data['Stock']

    j = boll(data[i]['close'], include=False, length=14, fillna=True)
    v = adx(data[i], include=False, length=14, fillna=True)

    k = pd.concat([data[i], j], axis=1)
    k = pd.concat([k, v], axis=1)

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
        if row['DI+(14)'] > row['DI-(14)'] + DI_UPPER:
            condition = "Sell"
        elif row['DI-(14)'] > row['DI+(14)'] + DI_LOWER:
            condition = "Buy"
        else:
            condition = "Hold"
        new_row = pd.DataFrame({'ADX': row['ADX(14)'], 'DI+': row['DI+(14)'], 'DI-': row['DI-(14)'],
                                'ADX Condition': condition, 'Volume': row['volume']}, index=[0])
        adx_results = pd.concat(
            [adx_results, new_row], ignore_index=True)
    return adx_results

def Aggr_Results():
    results = pd.concat(
    [Boll_Results(stock_data), ADX_Results(stock_data)], axis=1)
            
    aggr_results = pd.DataFrame(columns=['Index', 'Close', 'Upper', 'Lower', 'Boll Condition',
                                'ADX', 'DI+', 'DI-', 'ADX Condition', 'Aggr Condition', 'Volume'])
    price = 0
    for index, row in results.iterrows():
        if row['ADX Condition'] == "Buy":  # row['Boll Condition'] == "Buy" or
            condition = "Buy"
            price = row['Close']
        elif row['ADX Condition'] == "Sell" and row["Close"] > price:
            condition = "Sell"
        else:
            condition = "Hold"

        # if row['ADX Condition'] == "Buy":
        #     condition = "Buy"
        # elif row['ADX Condition'] == "Sell":
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
    cycle_cost = 0
    cycle_count = 0
    total_gain = 0
    total_stocks_bought = 0
    INITIAL_INVESTMENT = 100000
    is_buying = False
    for index, row in aggr_results.iterrows():
        if row['Aggr Condition'] == "Buy" and not is_buying and INITIAL_INVESTMENT > row["Close"]:
            is_buying = True
            cycle_number_of_stocks = 1
            total_stocks_bought += 1
            cycle_count += 1
            cycle_cost -= row['Close']
            INITIAL_INVESTMENT -= row['Close']
            running_cost -= row['Close']
            start_date = row['Index']
            print(
                f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}")
            sold = False
        elif is_buying:
            if row['Aggr Condition'] == "Sell":
                is_buying = False
                cycle_revenue = ((total_stocks_bought) * row['Close'])
                INITIAL_INVESTMENT += cycle_revenue

                print(
                    f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}\n")
                cycle_gain = round((cycle_revenue + cycle_cost) /
                                    abs(cycle_cost)*100, 2)
                total_gain += cycle_gain
                stop_date = row['Index']
                cycle_number_of_stocks = 0
                print(
                    f"The lap gain is {cycle_gain} from {start_date} to {stop_date}\nWith a cost of {round(-cycle_cost,2)}\nAnd a revenue of {round(cycle_revenue,2)}\n")
                cycle_revenue = 0
                cycle_cost = 0
                total_stocks_bought = 0

            elif INITIAL_INVESTMENT > row["Close"]:
                # cycle_number_of_stocks = 1
                # total_stocks_bought += cycle_number_of_stocks
                # cycle_cost -= row['Close']*cycle_number_of_stocks
                
                # INITIAL_INVESTMENT -= row['Close']*cycle_number_of_stocks
                
                sold = False
                print(
                    f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}")
            else:
                print(
                    f"No stocks purchased")
                
    # try:
    #     total_gain = (
    #         ((running_revenue + (running_cost - cycle_cost))/abs(running_cost))*100)
    # except ZeroDivisionError:
    #     total_gain = 0
    try:
        average_cycle_gain = round(total_gain/cycle_count,2)
    except ZeroDivisionError:
        average_cycle_gain = 0
    print(
        f"\nTotal Cost to Date (Including Held Positions): {round(-running_cost + cycle_cost,2)}")
    print(
        f"\nTotal Cost in Held Positions): {round(-running_cost,2)}")
    print(
        f"Total Revenue to Date (Excluding Held Positions): {round(running_revenue,2)}")
    print(
        f"Total Gain over Investment Period: {round(total_gain,2)}")
    try:
        print(
            f"Average Full Cycle Gain: {average_cycle_gain} over {cycle_count} cycles\n")
    except ZeroDivisionError:
        print(f"Average Full Cycle Gain: {round(0,2)}\n")
    print(f"DI Upper for this test is {DI_UPPER}")
    print(f"DI Lower for this test is {DI_LOWER}\n")
    try:
        actual_gain = ((INITIAL_INVESTMENT-100000)/-running_cost)*100
    except ZeroDivisionError:
        actual_gain = 0

    global BEST_GAIN
    global BEST_CYCLE_GAIN
    if actual_gain > BEST_GAIN:
        BEST_GAIN = actual_gain
        global BEST_UPPER_ACTUAL
        BEST_UPPER_ACTUAL = DI_UPPER
        global BEST_LOWER_ACTUAL
        BEST_LOWER_ACTUAL = DI_LOWER


    if average_cycle_gain > BEST_CYCLE_GAIN:
        BEST_GAIN = actual_gain
        BEST_CYCLE_GAIN = average_cycle_gain
        global BEST_UPPER_CYCLE
        BEST_UPPER_CYCLE = DI_UPPER
        global BEST_LOWER_CYCLE
        BEST_LOWER_CYCLE = DI_LOWER

    print(
        f" The best gain is {BEST_GAIN}, with a Best Upper Actual of {BEST_UPPER_ACTUAL}, and a Best Lower Actual of {BEST_LOWER_ACTUAL}")
    print(
        f" The best cycle gain is {BEST_CYCLE_GAIN}, with a Best Upper Cycle of {BEST_UPPER_CYCLE}, and a Best Lower Cycle of {BEST_LOWER_CYCLE}")
    print(INITIAL_INVESTMENT)
    print(actual_gain)

DI_UPPER = 0  # 7
DI_LOWER = 0  # 15
symbols = get_ticker_symbols()
ticker = 1 #change this back to i when you put it back in the for loop
print(ticker)

for date_index in range(0, -365, -1):

    for upper_index in range(0, 51):

        for lower_index in range(0, 51):

        
        # for i in symbols:
            stock_data = Get_Data(ticker,date_index)
            Analyze_Results()
            print(f"The increment for this test is {date_index}")
            print(FULL_SET)
            print("\n")
        
            
            DI_LOWER += 1

        DI_LOWER = 0
        DI_UPPER += 1
    global best_settings_dict
    best_settings_dict = {
                    f"Date Index {date_index}" : 
                        {
                        "Best Upper Actual" : BEST_UPPER_ACTUAL, 
                        "Best Lower Actual" : BEST_LOWER_ACTUAL, 
                        "Best Gain" : BEST_GAIN,
                        "Best Upper Cycle" : BEST_UPPER_CYCLE,
                        "Best Lower Cycle" : BEST_LOWER_CYCLE,
                        "Best Cycle Gain" : BEST_CYCLE_GAIN
                        }
                    }
    global best_settings
    best_settings = [date_index, BEST_UPPER_ACTUAL, BEST_LOWER_ACTUAL, BEST_GAIN, BEST_UPPER_CYCLE, BEST_LOWER_CYCLE, BEST_CYCLE_GAIN]
    FULL_SET.append(best_settings)
    DI_LOWER = 0
    DI_UPPER = 0
    BEST_GAIN = 0
    BEST_CYCLE_GAIN = 0
    INITIAL_INVESTMENT = 100000
    running_cost = 0
print(FULL_SET)
print(best_settings_dict)