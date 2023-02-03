import pandas as pd
from yahoo_fin import stock_info
from datetime import datetime, timedelta
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import numpy as np
from alive_progress import alive_bar
import time
import pmdarima as pm
# from keras.models import Sequential
# from keras.layers import Dense
from statsmodels.tsa.arima.model import ARIMA
from scipy.fftpack import fft
import warnings


pd.options.mode.chained_assignment = None
warnings.simplefilter('ignore')

CYCLES = 1000
TICKER = "GOOG"



total_accuracy = 0
prediction_list = []
num_lr = 0
total_accuracy_rf = 0
prediction_list_rf = []
num_rf = 0
prediction = None
prediction_rf = None

with alive_bar(CYCLES, force_tty=True) as bar:

    for i in range(CYCLES):

        # Get the historical stock data for the last 10 years
        start_date = datetime.now() - timedelta(days=365*.5)
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

        # Perform linear regression analysis
        stock_data = stock_data.dropna()
        stock_data["label"] = stock_data["close"].shift(-1).dropna()
        x = stock_data[["close", "upper_band", "lower_band", "14_day_adx", "avg_gain", "avg_loss",
                        "rs", "rsi", "26_day_ema", "12_day_ema", "macd", "signal", "histogram"]].shift(1).dropna()
        # x = x[:-1]
        x = preprocessing.scale(x)
        y = stock_data["label"].dropna()
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2, train_size=0.8)
        model = LinearRegression().fit(x_train, y_train)
        accuracy = model.score(x_test, y_test)

        # Create and train Random Forest model
        rf_model = RandomForestRegressor(
            n_estimators=1000).fit(x_train, y_train)
        rf_accuracy = rf_model.score(x_test, y_test)

    
        # # Create a neural network model
        # model = Sequential()
        # model.add(Dense(64, activation='relu', input_shape=(x_train.shape[1],)))
        # model.add(Dense(64, activation='relu'))
        # model.add(Dense(1, activation='linear'))
        # model.compile(optimizer='adam', loss='mse')

        # # Train the model on the training data
        # model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=1)

        # # Evaluate the model on the test data
        # score = model.evaluate(x_test, y_test, verbose=0)
        # print("Test loss:", score)
        # # Use the trained model to make predictions on new data
        # predictions = model.predict(x_test)

        # Print results
        print("Linear regression model accuracy:", accuracy)
        print("Random Forest model accuracy:", rf_accuracy)
        # print("ARIMA model prediction:", prediction_arima)
        # print("Neural Network model loss:", score)
        # print("Neural Network model prediction:", predictions[0])

        # # Plot results
        # plt.plot(stock_data["close"])
        # plt.plot(stock_data["20_day_sma"])
        # plt.plot(stock_data["upper_band"])
        # plt.plot(stock_data["lower_band"])
        # plt.title("Bollinger Bands for Apple Stock")
        # plt.xlabel("Date")
        # plt.ylabel("Stock Price")
        # plt.show()

        # plt.plot(stock_data["14_day_adx"])
        # plt.title("ADX for Apple Stock")
        # plt.xlabel("Date")
        # plt.ylabel("ADX")
        # plt.show()

        # plt.plot(stock_data["rsi"])
        # plt.title("RSI for Apple Stock")
        # plt.xlabel("Date")
        # plt.ylabel("RSI")
        # plt.show()

        # plt.plot(stock_data["macd"])
        # plt.plot(stock_data["signal"])
        # plt.title("MACD for Apple Stock")
        # plt.xlabel("Date")
        # plt.ylabel("MACD/Signal")
        # plt.show()

        # plt.scatter(x_test[:, 0], y_test)
        # plt.plot(x_test[:, 0], model.predict(x_test), color="r")
        # plt.title("Linear Regression for Apple Stock")
        # plt.xlabel("Close Price")
        # plt.ylabel("Predicted Next Close Price")
        # plt.show()

        # #code for automatic resistance level identification
        # stock_data["resistance"] = 0
        # stock_data["resistance"][stock_data["close"] > stock_data["close"].rolling(window=50).max()] = 1
        # plt.scatter(stock_data.index, stock_data["close"], c=stock_data["resistance"])
        # plt.title("Resistance Levels for Apple Stock")
        # plt.xlabel("Date")
        # plt.ylabel("Stock Price")
        # plt.show()

        # #Plot the linear regression line
        # plt.scatter(x_test[:, 0], y_test)
        # plt.plot(x_test[:, 0], model.predict(x_test), color="r")
        # plt.title("Linear Regression for Apple Stock")
        # plt.xlabel("Close Price")
        # plt.ylabel("Predicted Next Close Price")
        # plt.show()

        # Get the input features for the next day
        next_day_features = x_test[0]

        # Use the linear regression model to predict the next day's stock price
        next_day_prediction_lr = model.predict([next_day_features])

        # print("Predicted stock price for next day: ", next_day_prediction_lr)

        # Use the Random Forest model to predict the next day's stock price
        next_day_prediction_rf = rf_model.predict([next_day_features])

        # print("Predicted stock price for next day: ", next_day_prediction_rf)

        if accuracy > 0.8:
            total_accuracy += accuracy
            num_lr += 1
            prediction_list.append(next_day_prediction_lr)
            prediction = sum(prediction_list)/len(prediction_list)

        if rf_accuracy > 0.8:
            total_accuracy_rf += rf_accuracy
            num_rf += 1
            prediction_list_rf.append(next_day_prediction_rf)
            prediction_rf = sum(prediction_list_rf)/len(prediction_list_rf)
        # time.sleep(0.03)
        bar()

    try:
        print("Average accuracy for linear regression model:",
              total_accuracy / num_lr)
    except ZeroDivisionError:
        print("No accuracy above 90% for linear regression model")
    try:
        print("Average accuracy for Random Forest model:",
              total_accuracy_rf / num_rf)
    except ZeroDivisionError:
        print("No accuracy above 90% for Random Forest model")
    print("Predicted LR stock price for next day: ", prediction)
    print("Predicted RF stock price for next day: ", prediction_rf)
    # print("Predicted ARIMA stock price for next day: ", prediction_arima)
    # print(stock_data)
    # print(x_test)
