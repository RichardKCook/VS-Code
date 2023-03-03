import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from yahoo_fin import stock_info
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import talib
from statsmodels.tsa.arima.model import ARIMA
import sys
import requests
import json
np.set_printoptions(threshold=sys.maxsize)

# Import stock data using yfinance
NAME = "GOOG"
df = stock_info.get_data(f"{NAME}", start_date='01-01-2022', end_date='02-07-2023')
df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = df[['open', 'high', 'low', 'close', 'adjclose', 'volume']]
df.drop(columns=['open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker'], inplace=True)
df = df.reset_index()
df.rename(columns={'index': 'Date'}, inplace=True)
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

with open("/Users/Cook/Documents/API Keys/StockNewsAPI.txt", mode="r") as f:
    API_KEY = f.readline()
    f.close

# Read the contents of the file into a variable
try:
    with open("/Users/Cook/Documents/API Keys/StockNewsAPI.json", "r") as f:
        old_data = json.load(f)
except FileNotFoundError:
    with open("/Users/Cook/Documents/API Keys/StockNewsAPI.json", "w") as f:
        old_data = {}
        json.dump(old_data, f, indent=4)

# # Get the new data
# new_data = requests.get(f"https://stocknewsapi.com/api/v1?tickers={NAME}&items=100&page=1&token={API_KEY}").json()

# # Update the old data with the new data
# old_data.update(new_data)

# # Write the combined data back to the file
# with open("/Users/Cook/Documents/API Keys/StockNewsAPI.json", "w") as f:
#     json.dump(old_data, f, indent=4)

with open("/Users/Cook/Documents/API Keys/StockNewsAPI.json", mode="r") as f:
    articles = json.load(f)
    f.close

# Create a new list to store the transformed data
transformed_data = []

# Loop through the data in the "data" key of the json data
for item in articles['data']:
    # Extract the sentiment value and convert it to a numerical value
    if item['sentiment'] == 'Positive':
        sentiment_value = 1
    elif item['sentiment'] == 'Neutral':
        sentiment_value = 0
    else:
        sentiment_value = -1

    # Add the sentiment value to the transformed data
    transformed_data.append({
        'Date': item['date'],
        'Sentiment': sentiment_value
    })

# Convert the transformed data into a pandas dataframe
article_df = pd.DataFrame(transformed_data)


df = df.set_index("Date")
article_df['Date'] = pd.to_datetime(article_df['Date'])
article_df['Date'] = article_df['Date'].dt.strftime('%Y-%m-%d')
article_df = article_df.groupby('Date').sum()
# Merge the two dataframes on the 'Date' column
df = pd.merge(df, article_df, on='Date', how='left')
df.index = pd.to_datetime(df.index)

# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(df)


# Calculate technical indicators
df['SMA_20'] = df['Close'].rolling(window=20).mean()
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['RSI'] = talib.RSI(df['Close'].values, timeperiod=14)
df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'].values, fastperiod=12, slowperiod=26, signalperiod=9)
df['ADX'] = talib.ADX(df['High'].values, df['Low'].values, df['Close'].values, timeperiod=14)
df['DMI_PLUS'], df['DMI_MINUS'] = talib.PLUS_DI(df['High'].values, df['Low'].values, df['Close'].values, timeperiod=14), talib.MINUS_DI(df['High'].values, df['Low'].values, df['Close'].values, timeperiod=14)



# Split data into train and test sets
train_data = df[df.index < datetime(2022,6,1)].astype(float)
test_data = df[df.index >= datetime(2022,6,1)].astype(float)

timesteps = 30
# Preprocessing for LSTM
train_data_temp = np.array(train_data[['Close','Open','High','Low','Volume','Sentiment','SMA_20','SMA_50','RSI','MACD','MACD_signal','MACD_hist','ADX','DMI_PLUS','DMI_MINUS']].values)
train_data_LSTM = train_data_temp.reshape(-1, 15)
scaler = MinMaxScaler(feature_range=(0, 1))
train_data_LSTM = scaler.fit_transform(train_data_LSTM)

# Train LSTM

n_future = 1
X_train = []
y_train = []
for i in range(timesteps, len(train_data_LSTM) - n_future + 1):
    X_train.append(train_data_LSTM[i-timesteps:i, 0:train_data_LSTM.shape[1]])
    y_train.append(train_data_LSTM[i + n_future - 1:i + n_future, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

print(f'X_train shape == {X_train.shape}')
print(f'y_train shape == {y_train.shape}')

model = Sequential()
model.add(LSTM(units=128, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(units=128))
model.add(Dense(units=1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, y_train, epochs=100, batch_size=64)

# # Predict with LSTM
# test_data_temp = np.array(test_data[['Close','Open','High','Low','Volume','Sentiment','SMA_20','SMA_50','RSI','MACD','MACD_signal','MACD_hist','ADX','DMI_PLUS','DMI_MINUS']].values)
# test_data_LSTM = test_data_temp.reshape(-1, 15)
# test_data_LSTM = scaler.transform(test_data_LSTM)
# X_test = []
# for i in range(timesteps, len(test_data_LSTM) - n_future + 1):
#     X_test.append(test_data_LSTM[i + n_future - 1:i + n_future, 0])
# X_test = np.array(X_test)
# # X_test = np.array(X_test).reshape(-1, timesteps, 1)
# X_test = np.reshape(X_test, (len(X_test), timesteps, 15))

# Predict with LSTM
test_data_temp = np.array(test_data[['Close','Open','High','Low','Volume','Sentiment','SMA_20','SMA_50','RSI','MACD','MACD_signal','MACD_hist','ADX','DMI_PLUS','DMI_MINUS']].values)
test_data_LSTM = test_data_temp.reshape(-1, 15)
test_data_LSTM = scaler.transform(test_data_LSTM)
X_test = []
for i in range(timesteps, len(test_data_LSTM)):
    X_test.append(test_data_LSTM[i-timesteps:i, :])
X_test = np.array(X_test)


n_future = 14

lstm_pred = model.predict(X_train[-n_future:])
lstm_pred = np.repeat(timesteps, train_data_LSTM.shape[1], axis = -1)
lstm_pred = lstm_pred.reshape(-1, 15)
lstm_pred = scaler.inverse_transform(lstm_pred)[:,0]

# Combine predictions from LSTM and ARIMA
ensemble_pred = lstm_pred
print(ensemble_pred)

# Plot the actual vs predicted stock prices
plt.plot(test_data['Close'].values, color='red', label='Actual Stock Price')
plt.plot(ensemble_pred, color='blue', label='Predicted Stock Price')
plt.title(f'{NAME} Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.gca().invert_xaxis()
plt.show()













































# # Preprocessing for LSTM
# train_data_temp = train_data.copy()
# train_data_LSTM = np.array(train_data_temp).reshape(-1, 1)
# scaler = MinMaxScaler(feature_range=(0, 1))
# train_data_LSTM = scaler.fit_transform(train_data_LSTM)




# # Train LSTM
# timesteps = 30
# X_train = []
# y_train = []
# for i in range(timesteps, train_data_LSTM.shape[0]):
#     X_train.append(train_data_LSTM[i-timesteps:i, 0])
#     y_train.append(train_data_LSTM[i, 0])
# X_train, y_train = np.array(X_train), np.array(y_train)
# X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# model = Sequential()
# model.add(LSTM(units=128, return_sequences=True, input_shape=(X_train.shape[1], 1)))
# model.add(LSTM(units=128))
# model.add(Dense(units=1))
# model.compile(loss='mean_squared_error', optimizer='adam')
# model.fit(X_train, y_train, epochs=100, batch_size=64)



# # # Preprocessing for ARIMA
# # train_data_arima = np.array(train_data.Close)

# # Train ARIMA
# # model_arima = ARIMA(train_data_arima, order=(3,1,0))
# # model_arima_fit = model_arima.fit()

# # Predict with LSTM
# model.add(Dense(1))
# model.compile(loss='mean_squared_error', optimizer='adam')
# model.fit(X_train, y_train, epochs=100, batch_size=32)

# test_data_temp = test_data

# test_data_LSTM = np.array(test_data_temp).reshape(-1, 1)
# test_data_LSTM = scaler.transform(test_data_LSTM)
# X_test = []
# for i in range(timesteps, test_data_LSTM.shape[0]):
#     X_test.append(test_data_LSTM[i-timesteps:i, 0])
# X_test = np.stack(X_test)
# X_test = np.reshape(X_test, (len(X_test), timesteps, 1))

# lstm_pred = model.predict(X_test)
# lstm_pred = scaler.inverse_transform(lstm_pred)

# # Predict with ARIMA
# # start = len(train_data_arima)
# # end = len(train_data_arima) + len(test_data) - 1
# # arima_pred = model_arima_fit.predict(start=start, end=end, typ='levels')

# # Combine predictions from LSTM and ARIMA
# ensemble_pred = lstm_pred
# print(ensemble_pred)

# # Plot the actual vs predicted stock prices
# plt.plot(test_data['Close'].values, color='red', label='Actual Stock Price')
# plt.plot(ensemble_pred['Close'], color='blue', label='Predicted Stock Price')
# plt.title('Apple Inc. Stock Price Prediction')
# plt.xlabel('Time')
# plt.ylabel('Stock Price')
# plt.legend()
# plt.gca().invert_xaxis()
# plt.show()