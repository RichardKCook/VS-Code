import requests
import json
from datetime import datetime, timedelta
import pytz
from time import sleep
from multiprocessing import Pool, Manager
from finrl.config_tickers import DOW_30_TICKER

API_KEY = "jjhoo2v1s8ia0s9z8dkik8yoj3vjngv0fwvxepdg"
API_ENDPOINT = "https://stocknewsapi.com/api/v1/stat"
FILE_NAME = "/Users/Cook/Documents/VS Code/Sentiment.json"
FIRST_SAVE = True

TICKERS = DOW_30_TICKER

for TICKER in TICKERS:
    def get_data(start_date, end_date, page):
        data = {}
        params = {
            "tickers": TICKER,
            "page": page,
            "date": start_date.strftime("%m%d%Y") + "-" + end_date.strftime("%m%d%Y"),
            "token": API_KEY
        }
        
        try:
            response = requests.get(API_ENDPOINT, params=params)
            if response.status_code == 200:
                json_data = response.json()
                if not json_data['data']:
                    return None, None
                pages = json_data['total_pages']

                for date, item in json_data['data'].items():
                    ticker = item[TICKER]
                    sentiment = ticker["sentiment_score"]
                    positive = ticker["Positive"]
                    negative = ticker["Negative"]
                    neutral = ticker["Neutral"]
                    data[date] = {
                        TICKER: {
                            "sentiment": sentiment,
                            "positive": positive,
                            "negative": negative,
                            "neutral": neutral
                        }
                    }
                return data, pages
            else:
                print("Error:", response.status_code)
                return None

        except requests.exceptions.Timeout:
            print("Connection timed out")
            sleep(300)
            get_data(start_date, end_date, page)
            return None


    def save_data(data, shared_file):
        print("Saving data...")

        with shared_file:
            try:
                with open(FILE_NAME, 'r') as f:
                    existing_data = json.load(f)
            except FileNotFoundError:
                existing_data = {}

            # Update data
            for date, tickers in data.items():
                if date in existing_data:
                    existing_data[date].update(tickers)
                else:
                    existing_data[date] = tickers

            # Save data
            with open(FILE_NAME, 'w') as f:
                json.dump(existing_data, f, indent=4)

        data.clear()

    def start():
        timezone = pytz.timezone('US/Eastern')
        current_date = datetime.now(timezone)
        earliest_date = None
        try:
            with open(FILE_NAME, 'r+') as f:
                try:
                    data = json.load(f)
                except json.decoder.JSONDecodeError:
                    data = {}
        except FileNotFoundError:
            print("File not found, creating new file.")
            data = {}

        end_date = current_date #use this to gather the most up-to-date data
        try:
            pass
            # end_date = datetime.strptime(list(data.keys())[0], "%Y-%m-%d") #use this to gather historical data
        except IndexError:
            end_date = current_date

        yesterday = current_date - timedelta(days=2)
        start_date = date_object = yesterday #datetime.strptime("01-01-2015", '%m-%d-%Y')

        manager = Manager()
        shared_data = manager.dict()
        shared_file = manager.Lock()

        while earliest_date is None or earliest_date > datetime(1999, 12, 31):
            print("Getting data for", start_date.strftime("%m/%d/%Y"), "-", end_date.strftime("%m/%d/%Y"))
            page = 1
            while True:
                print(f"Getting data for {TICKER}", start_date.strftime("%m/%d/%Y"), "-", end_date.strftime("%m/%d/%Y"), "on page", page)
            
                new_data, pages = get_data(start_date, end_date, page)
                
                if new_data and pages is not None:
                    shared_data.update(new_data)
                    page += 1
                    if page > pages:
                        pool = Pool()
                        pool.apply_async(save_data, args=(shared_data, shared_file))
                        pool.close()
                        pool.join()
                        # earliest_date = datetime.strptime(shared_data[-1]['date'], "%a, %d %b %Y %H:%M:%S %z")
                        # The following line assumes that the JSON structure has a "data" key with a dictionary of dates as its value
                        break
                        earliest_date_str = min(shared_data.keys())
                        earliest_date = datetime.strptime(earliest_date_str, "%Y-%m-%d")
                        shared_data = manager.dict()
                        break
                else:
                    pool = Pool()
                    pool.apply_async(save_data, args=(shared_data, shared_file))
                    pool.close()
                    pool.join()
                    # earliest_date = datetime.strptime(shared_data[-1]['date'], "%a, %d %b %Y %H:%M:%S %z")
                    # The following line assumes that the JSON structure has a "data" key with a dictionary of dates as its value
                    # earliest_date_str = min(shared_data[-1].keys())
                    # earliest_date = datetime.strptime(earliest_date_str, "%Y-%m-%d")
                    shared_data = manager.dict()
                    break
            break
            start_date = earliest_date - timedelta(days=30)
            end_date = earliest_date

        print("Finished gathering data.")

    if __name__ == "__main__":
        start()