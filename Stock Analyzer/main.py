"""

This is the main file for my Stock Analyzer project. 
It will be used to run the program and call the functions from the functions.py file.

***THIS IS NOT FOR INVESTMENT PURPOSES, USE AT YOUR OWN RISK***

***I AM NOT RESPONSIBLE FOR ANY LOSSES YOU MAY INCUR***

Author: Richard Cook
Created on 1/20/2023
Last Updated: 1/22/2023

Copyright 2023, all rights reserved.

"""



import pandas as pd
from yahoo_fin import stock_info
from plotly.offline import plot
# from plotly.offline import init_notebook_mode
# init_notebook_mode()
import plotly
import cufflinks as cf
cf.set_config_file(offline=True)
setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)
import os, sys
from functions import boll
from functions import adx


TICKER = "PYPL"
NUM_OF_TICKERS = 1

watchlist_path = "/Users/Cook/Documents/VS Code/Stock Analyzer/Yahoo Ticker Symbols - September 2017.csv"


def get_ticker_symbols():
    
    tickers = pd.read_csv(watchlist_path)
    ticker_symbols = tickers["Ticker"].iloc[0:NUM_OF_TICKERS]
    
    return ticker_symbols






# Get the data
def Get_Data(i):
    data = {}
    
    data[i] = stock_info.get_data(f"{i}", start_date='01-01-2013',  end_date='11-19-2022')
    


    # data = {}
    # data['Stock'] = stock_info.get_data(f"{TICKER}", start_date='01-01-2022',  end_date='01-20-2023')
    # print(data['AAPL'].head())
    # print(data["AAPL"])

    qf = cf.QuantFig(data[i])
    qf.add_bollinger_bands(boll_std=2)
    # qf.add_macd()
    # qf.add_rsi()
    qf.add_dmi()
    qf.iplot()


    # h= print(data['TSLA'])

    # i = data['Stock']

    j = boll(data[i]['close'], include= False, length=14, fillna=True)
    v = adx(data[i], include= False, length=14, fillna=True)

    k = pd.concat([data[i],j], axis=1)
    k = pd.concat([k,v], axis=1)

    # print(type(i))

    # print(type(j))

    # print(k)
    return k

def Boll_Results(k):
    boll_results = pd.DataFrame(columns=['Index', 'Close', 'Upper', 'Lower', 'Boll Condition'])
    for index, row in k.iterrows():
        if row['high'] > row['UPPER(close,20)']:
            condition = "Sell"
        elif row['low'] < row['LOWER(close,20)']:
            condition = "Buy"
        else:
            condition = "Hold"
        new_row = pd.DataFrame({'Index': index, 'Close': row['close'], 'Upper': row['UPPER(close,20)'], 'Lower': row['LOWER(close,20)'], 'Boll Condition': condition}, index=[0])
        boll_results = pd.concat([boll_results, new_row], ignore_index=True)
    return boll_results
# boll_results = pd.DataFrame(columns=['Index', 'Close', 'Upper', 'Lower', 'Boll Condition'])
# for index, row in k.iterrows():
#     if row['high'] > row['UPPER(close,20)']:
#         condition = "Sell"
#     elif row['low'] < row['LOWER(close,20)']:
#         condition = "Buy"
#     else:
#         condition = "Hold"
#     new_row = pd.DataFrame({'Index': index, 'Close': row['close'], 'Upper': row['UPPER(close,20)'], 'Lower': row['LOWER(close,20)'], 'Boll Condition': condition}, index=[0])
#     boll_results = pd.concat([boll_results, new_row], ignore_index=True)

def ADX_Results(k):
    adx_results = pd.DataFrame(columns=['ADX', 'DI+', 'DI-', 'ADX Condition'])
    for index, row in k.iterrows():
        if  row['DI+(14)'] > row['DI-(14)'] + 7:
            condition = "Sell"
        elif row['DI-(14)'] > row['DI+(14)'] + 15:
            condition = "Buy"
        else:
            condition = "Hold"
        new_row = pd.DataFrame({'ADX': row['ADX(14)'], 'DI+': row['DI+(14)'], 'DI-': row['DI-(14)'], 'ADX Condition': condition, 'Volume': row['volume']}, index=[0])
        adx_results = pd.concat([adx_results, new_row], ignore_index=True)
    return adx_results

# adx_results = pd.DataFrame(columns=['ADX', 'DI+', 'DI-', 'ADX Condition'])
# for index, row in k.iterrows():
#     if  row['DI+(14)'] > row['DI-(14)'] + 7:
#         condition = "Sell"
#     elif row['DI-(14)'] > row['DI+(14)'] + 15:
#         condition = "Buy"
#     else:
#         condition = "Hold"
#     new_row = pd.DataFrame({'ADX': row['ADX(14)'], 'DI+': row['DI+(14)'], 'DI-': row['DI-(14)'], 'ADX Condition': condition, 'Volume': row['volume']}, index=[0])
#     adx_results = pd.concat([adx_results, new_row], ignore_index=True)

# results = pd.concat([boll_results, adx_results], axis=1)

# print(results)
def Aggr_Results():
    results = pd.concat([Boll_Results(stock_data), ADX_Results(stock_data)], axis=1)
    aggr_results = pd.DataFrame(columns=['Index', 'Close', 'Upper', 'Lower', 'Boll Condition', 'ADX', 'DI+', 'DI-', 'ADX Condition', 'Aggr Condition','Volume'])
    for index, row in results.iterrows():
        if row['Boll Condition'] == "Buy" or row['ADX Condition'] == "Buy":
            condition = "Buy"
        elif row['ADX Condition'] == "Sell":
            condition = "Sell"
        else:
            condition = "Hold"

        # if row['ADX Condition'] == "Buy":
        #     condition = "Buy"
        # elif row['ADX Condition'] == "Sell":
        #     condition = "Sell"
        # else:
        #     condition = "Hold"


        new_row_aggr = pd.DataFrame({'Index': row['Index'],'Close': row['Close'], 'Upper': row['Upper'], 'Lower': row['Lower'], 'Boll Condition': row['Boll Condition'], 'ADX': row['ADX'], 'DI+': row['DI+'], 'DI-': row['DI-'], 'ADX Condition': row['ADX Condition'], 'Aggr Condition': condition, 'Volume': row['Volume']}, index=[0])
        aggr_results = pd.concat([aggr_results, new_row_aggr], ignore_index=True)
    return aggr_results


# aggr_results = pd.DataFrame(columns=['Index', 'Close', 'Upper', 'Lower', 'Boll Condition', 'ADX', 'DI+', 'DI-', 'ADX Condition', 'Aggr Condition'])
# for index, row in results.iterrows():
#     if row['Boll Condition'] == "Buy" or row['ADX Condition'] == "Buy":
#         condition = "Buy"
#     elif row['ADX Condition'] == "Sell":
#         condition = "Sell"
#     else:
#         condition = "Hold"

#     # if row['ADX Condition'] == "Buy":
#     #     condition = "Buy"
#     # elif row['ADX Condition'] == "Sell":
#     #     condition = "Sell"
#     # else:
#     #     condition = "Hold"


#     new_row_aggr = pd.DataFrame({'Index': row['Index'],'Close': row['Close'], 'Upper': row['Upper'], 'Lower': row['Lower'], 'Boll Condition': row['Boll Condition'], 'ADX': row['ADX'], 'DI+': row['DI+'], 'DI-': row['DI-'], 'ADX Condition': row['ADX Condition'], 'Aggr Condition': condition, 'Volume': row['Volume']}, index=[0])
#     aggr_results = pd.concat([aggr_results, new_row_aggr], ignore_index=True)

def Analyze_Results():
    aggr_results = Aggr_Results()
    running_revenue = 0
    running_total = 0
    num = 1
    lap_revenue = 0
    lap_total = 0
    lap_count = 0
    sum_laps=0
    tot_apr = 0
    apr = 0
    
    is_buying = False
    for index, row in aggr_results.iterrows():
        if row['Aggr Condition'] == "Buy" and not is_buying:
            is_buying = True
            num += 1
            lap_count +=1
            lap_total -= row['Close']
            running_total -= row['Close']
            start_date = row['Index']
            print(f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}")
            sold = False
        elif is_buying:
            if row['Aggr Condition'] == "Sell":
                is_buying = False
                lap_revenue = ((num-1) * row['Close'])
                running_revenue += lap_revenue
                
                print(f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}\n")
                lap_gain = round((lap_revenue + lap_total)/abs(lap_total)*100,2)
                sum_laps +=lap_gain
                stop_date = row['Index']
                # try:
                #     apr = ((((lap_gain/100)/num)+1)**365 - 1)*100
                # except ZeroDivisionError:
                #     pass
                # print(apr)
                # print(num)
                num = 1
                tot_apr += apr
                print(f"The lap gain is {lap_gain} from {start_date} to {stop_date}\nWith a cost of {round(-lap_total,2)}\nAnd a revenue of {round(lap_revenue,2)}\n")
                lap_revenue = 0
                lap_total = 0
                
            else:
                num += 1
                lap_total -= row['Close']
                running_total -= row['Close']
                sold = False
                print(f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}")

    print(f"\nTotal Cost to Date (Including Held Positions): {round(-running_total,2)}")
    print(f"Total Revenue to Date (Excluding Held Positions): {round(running_revenue,2)}")
    print(f"Total Gain to Date: {round((running_revenue + running_total)/abs(running_total)*100,2)}")
    print(f"Full Cycle Gain Average: {round(sum_laps/lap_count,2)}")
    

    



# running_revenue = 0
# running_total = 0
# num = 0
# lap_revenue = 0
# lap_total = 0
# is_buying = False
# for index, row in aggr_results.iterrows():
#     if row['Aggr Condition'] == "Buy" and not is_buying:
#         is_buying = True
#         num += 1
#         lap_total -= row['Close']
#         running_total -= row['Close']
#         print(f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}")
#     elif is_buying:
#         if row['Aggr Condition'] == "Sell":
#             is_buying = False
#             lap_revenue = lap_revenue + (num * row['Close'])
#             running_revenue += lap_revenue
#             num = 0
#             print(f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}\n")
#             lap_gain = (lap_revenue + lap_total)/abs(lap_total)*100
#             print(f"{lap_gain}\n")
#             lap_revenue = 0
#             lap_total = 0
#         else:
#             num += 1
#             lap_total -= row['Close']
#             running_total -= row['Close']
#             print(f"{row['Aggr Condition']} at {round(float(row['Close']),2)} on {row['Index']} with {row['Volume']}")

# running_gain = (running_revenue + running_total)/abs(running_total)*100

            
# print(-running_total, running_revenue, running_gain)

    
   
            

symbols = get_ticker_symbols()

for i in symbols:
    ticker = i
    print(ticker)
    stock_data = Get_Data(ticker)
    Analyze_Results()
    print("\n")



