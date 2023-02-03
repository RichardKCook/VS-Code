from yahoo_fin import stock_info
from datetime import datetime, timedelta
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
from scipy.fftpack import fft
import warnings


warnings.simplefilter('ignore')

TICKER = "AAPL"

# Get the historical stock data for the last 10 years
end_date = datetime.now()
start_date = datetime.now() - timedelta(days=365*10)
stock_data = stock_info.get_data(TICKER, start_date=start_date)

# Perform Bollinger Bands analysis
stock_data["20_day_sma"] = stock_data["close"].rolling(
    window=20).mean()
stock_data["20_day_std"] = stock_data["close"].rolling(window=20).std()
stock_data["upper_band"] = stock_data["20_day_sma"] + \
    (stock_data["20_day_std"] * 2)
stock_data["lower_band"] = stock_data["20_day_sma"] - \
    (stock_data["20_day_std"] * 2)

# Perform ADX analysis
stock_data["up_move"] = stock_data["high"] - \
    stock_data["high"].shift(1)
stock_data["down_move"] = stock_data["low"].shift(
    1) - stock_data["low"]
stock_data["up_move"][stock_data["up_move"] < 0] = 0
stock_data["down_move"][stock_data["down_move"] < 0] = 0
stock_data["14_day_pos_dir"] = stock_data["up_move"].rolling(
    window=14).sum()
stock_data["14_day_neg_dir"] = stock_data["down_move"].rolling(
    window=14).sum()
stock_data["14_day_dx"] = (stock_data["14_day_pos_dir"] - stock_data["14_day_neg_dir"]) / (
    stock_data["14_day_pos_dir"] + stock_data["14_day_neg_dir"]) * 100
stock_data["14_day_adx"] = stock_data["14_day_dx"].rolling(
    window=14).mean()

# Calculate RSI
stock_data["delta"] = stock_data["close"] - \
    stock_data["close"].shift(1)
gain = stock_data["delta"][stock_data["delta"] > 0].sum()
loss = -stock_data["delta"][stock_data["delta"] < 0].sum()
stock_data["avg_gain"] = gain / 14
stock_data["avg_loss"] = loss / 14
stock_data["rs"] = stock_data["avg_gain"] / stock_data["avg_loss"]
stock_data["rsi"] = 100 - (100 / (1 + stock_data["rs"]))

# Perform EMA analysis
stock_data["26_day_ema"] = stock_data["close"].ewm(span=26).mean()
stock_data["12_day_ema"] = stock_data["close"].ewm(span=12).mean()

# Perform MACD analysis
stock_data["macd"] = stock_data["12_day_ema"] - \
    stock_data["26_day_ema"]
stock_data["signal"] = stock_data["macd"].ewm(span=9).mean()
stock_data["histogram"] = stock_data["macd"] - stock_data["signal"]

# Perform FFT
close_prices = stock_data["close"].values
fft_result = fft(close_prices)

# Extract magnitude of FFT coefficients
fft_magnitude = np.abs(fft_result)

# Add FFT magnitude to stock data
stock_data["fft_magnitude"] = fft_magnitude
# stock_data["fft_magnitude"] = np.fft.fftshift(stock_data["fft_magnitude"])


# Get the start and end date of the stock data
start_date = stock_data.index[0]
end_date = stock_data.index[-1]

# Create the date range using the start and end date of the stock data
date_range = pd.date_range(start_date, end_date, freq='D')

# Reindex the stock data using the date range
stock_data = stock_data.reindex(date_range)

# Drop any rows with missing values
stock_data.dropna(inplace=True)

# Define the p, d, and q parameters to try
p_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d_values = [0, 1, 2, 3, 4]
q_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of all possible combinations of p, d, and q
pdq = [(p, d, q) for p in p_values for d in d_values for q in q_values]

# Define the seasonal components
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in pdq]


# Split the stock data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    stock_data.index.to_pydatetime(), stock_data['close'], test_size=0.2, random_state=42, shuffle=False)

# Initialize a dictionary to store the results of the grid search
best_params = {}
lowest_mse = float('inf')


test_count = 1
# Iterate over all possible combinations of p, d, and q
for pdq_combination in pdq:
    # try:
    # Create an ARIMA model with the current combination of p, d, and q
    arima_model = ARIMA(y_train, order=pdq_combination,
                        enforce_stationarity=False, enforce_invertibility=False)

    # Fit the model to the training data
    arima_model_fit = arima_model.fit()

    # Convery x_test to a dataframe
    x_test_df = pd.DataFrame(x_test)
    x_test_df.index = pd.to_datetime(x_test_df.index)
    min_date = x_test_df.index.min()
    max_date = x_test_df.index.max()

    # Make predictions on the testing data
    predictions = arima_model_fit.predict(start=x_test_df.index.get_loc(x_test_df.first_valid_index(
    )), end=x_test_df.index.get_loc(x_test_df.last_valid_index()), typ='levels')
    predictions = predictions.dropna()

    # Calculate the mean squared error of the predictions
    mse = mean_squared_error(y_test, predictions)
    # If this combination of p, d, and q results in a lower MSE than the previous combination, update the best parameters
    if mse < lowest_mse:
        lowest_mse = mse
        best_params['pdq'] = pdq_combination
        best_params['mse'] = mse
    # except:
    #     print("I was passed")
    #     pass
    print(f"Test #{test_count}")
    test_count += 1

# Print the best p, d, and q values

print("Best p, d, q values: ", best_params.get('pdq'))

best_p, best_d, best_q = best_params['pdq']

# Create an ARIMA model with the best parameters
arima_model = ARIMA(np.asarray(
    stock_data['close']), order=(best_p, best_d, best_q))

# Fit the model to the data
arima_model_fit = arima_model.fit()


prediction_arima = arima_model_fit.forecast()[0]
print("ARIMA model prediction:", prediction_arima)
