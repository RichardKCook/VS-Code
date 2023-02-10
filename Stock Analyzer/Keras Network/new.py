import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from yahoo_fin import stock_info
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import talib
from statsmodels.tsa.arima.model import ARIMA
import sys
import requests
import json
import plotly.graph_objs as go
np.set_printoptions(threshold=sys.maxsize)




# Import stock data using yfinance
NAME = "GOOG"
df = stock_info.get_data(
    f"{NAME}", start_date='01-01-2000', end_date='02-09-2023')
df[['Open', 'High', 'Low', 'Close', 'Adj_Close', 'Volume']
   ] = df[['open', 'high', 'low', 'close', 'adjclose', 'volume']]
df.drop(columns=['open', 'high', 'low', 'close',
        'adjclose', 'volume', 'ticker'], inplace=True)
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
# df = pd.merge(df, article_df, on='Date', how='left') #Add ['Sentiment'] back to the index below when you add it back in
df.index = pd.to_datetime(df.index)




# Calculate technical indicators
df['SMA_20'] = df['Close'].rolling(window=20).mean()
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['RSI'] = talib.RSI(df['Close'].values, timeperiod=14)
df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(
    df['Close'].values, fastperiod=12, slowperiod=26, signalperiod=9)
df['ADX'] = talib.ADX(df['High'].values, df['Low'].values,
                      df['Close'].values, timeperiod=14)
df['DMI_PLUS'], df['DMI_MINUS'] = talib.PLUS_DI(df['High'].values, df['Low'].values, df['Close'].values, timeperiod=14), talib.MINUS_DI(
    df['High'].values, df['Low'].values, df['Close'].values, timeperiod=14)


# Split data into train and test sets
train_data = df[df.index <= datetime(2023, 2, 9)].astype(float)
# test_data = df[df.index >= datetime(2020, 1, 1)].astype(float)

# Get the number of datapoints in the train data
n_data = train_data.shape[0]

# Remove the nan values from the SMA_20 and SMA_50 columns
train_data = train_data.iloc[50:, :]
# test_data = test_data.iloc[50:, :]

# # Keep only the first (n-30) datapoints in the train data
# train_data = train_data.iloc[:n_data - n_data % 30, :]

# # Keep only the last (n-30) datapoints in the train data
# test_data = test_data.iloc[-n_data + n_data % 30:, :]

# Get the number of timesteps
timesteps = 30

# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(train_data)

# Initialize the StandardScaler object
scaler = StandardScaler()

# Convert the train data into a numpy array
train_data_temp = train_data[['Close','Open','High','Low','Volume','SMA_20','SMA_50','RSI','MACD','MACD_signal','MACD_hist','ADX','DMI_PLUS','DMI_MINUS']].values
y_train_temp = train_data[['Close']].shift(-1).dropna().values

# Keep only the last (n-30) datapoints in the train data
train_data_temp = train_data_temp[-n_data + n_data % 30:, :]
y_train_temp = y_train_temp[-n_data + n_data % 30:, :]

# Get the number of datapoints in the train data
n_data = train_data_temp.shape[0]
m_data = y_train_temp.shape[0]


# Keep only the last (n-30) datapoints in the train data
train_data_temp = train_data_temp[-n_data + n_data % 30:, :]
y_train_temp = y_train_temp[-m_data + m_data % 30:, :]




# Standardize the train data
train_data_temp = scaler.fit_transform(train_data_temp)
y_train_temp = scaler.fit_transform(y_train_temp)

# Initialize the X_train and y_train arrays
X_train = []
y_train = []

# Loop over the training data, creating a 30-day window and a next-day prediction for each iteration
j = 0
for i in range(len(train_data_temp)-timesteps):
    j+=1
    X_train.append(train_data_temp[i:i+timesteps, :])
    try:
        y_train.append(y_train_temp[i+timesteps-1])
    except IndexError:
        print(f"IndexError at {i}")
    # print(len(X_train))
    # print(len(y_train))


# Convert the X_train and y_train arrays to numpy arrays
X_train = np.array(X_train)
y_train = np.array(y_train)

# Reshape the X_train and y_train arrays into three-dimensional arrays
X_train = X_train.reshape(-1, timesteps, 14)
y_train = y_train.reshape(-1, 1)

# # Reshape the train data into a three-dimensional array
# X_train = train_data_temp.reshape(-1, timesteps, 14)
# y_train = y_train_temp.reshape(-1, timesteps, 1)


model = Sequential()
model.add(LSTM(units=128, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(units=128, return_sequences=True))
model.add(LSTM(units=128))
model.add(Dense(units=1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, y_train, epochs=100, batch_size=64)

print(f"The Shape of X_train is: {X_train.shape}")

X_train_reshaped = X_train.reshape(-1, X_train.shape[2])
X_train_inverted = scaler.inverse_transform(X_train_reshaped)

X_train_inverted_reshaped = X_train_inverted.reshape(X_train.shape)


prediction = model.predict(X_train_inverted_reshaped)


prediction_inverted = scaler.inverse_transform(prediction.reshape(-1, 1))
print(prediction_inverted)
# prediction_reshaped = prediction.reshape(-1, 1)
# prediction_inverted = scaler.inverse_transform(prediction_reshaped)


# print(prediction_inverted)

# print(y_train_temp)

# Actual data
actual = train_data['Close'].values

# Predicted data
prediction_inverted = scaler.inverse_transform(prediction.reshape(-1, 1))

# Create a new x-axis for the predicted values
x_pred = np.arange(len(actual), len(actual) + len(prediction_inverted))

# Plot the actual and predicted data
plt.plot(np.arange(len(actual)), actual, color='red', label='Actual Stock Price')
plt.plot(x_pred, prediction_inverted, color='blue', label='Predicted Stock Price')
plt.title(f'{NAME} Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()



# Actual data
actual = train_data['Close'].values

# Predicted data
prediction_inverted = scaler.inverse_transform(prediction.reshape(-1, 1))

fig = go.Figure(data=[go.Scatter(x=list(range(len(actual))), y=actual, name='Actual Stock Price', line=dict(color='red')),
                   go.Scatter(x=list(range(len(actual), len(actual) + len(prediction_inverted))), y=prediction_inverted.flatten(), name='Predicted Stock Price', line=dict(color='blue'))])
fig.update_layout(title=f'{NAME} Stock Price Prediction', xaxis_title='Time', yaxis_title='Stock Price')
fig.show()