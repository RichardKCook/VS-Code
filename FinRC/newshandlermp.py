import requests
import json
from datetime import datetime, timedelta
import pytz
from time import sleep
import ujson
from multiprocessing import Pool, Manager

API_KEY = "jjhoo2v1s8ia0s9z8dkik8yoj3vjngv0fwvxepdg"
API_ENDPOINT = "https://stocknewsapi.com/api/v1/category"
FILE_NAME = "stock_news2.json"
FIRST_SAVE = True


def get_data(start_date, end_date, page):
    data = []
    params = {
        "section": "alltickers",
        "items": 100,
        "page": page,
        "date": start_date.strftime("%m%d%Y") + "-" + end_date.strftime("%m%d%Y"),
        "token": API_KEY
    }
    try:
        response = requests.get(API_ENDPOINT, params=params)
        if response.status_code == 200:
            json_data = response.json()
            if not json_data['data']:
                return None
            for item in json_data['data']:
                data.append({
                    "date": item["date"],
                    "sentiment": item["sentiment"],
                    "tickers": item["tickers"]
                })
            return data
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
                existing_data = ujson.load(f)
        except FileNotFoundError:
            existing_data = []

        # Update data
        existing_data.extend(data)

        # Save data
        with open(FILE_NAME, 'w') as f:
            ujson.dump(existing_data, f, indent=4)

    data.clear()


def start():
    timezone = pytz.timezone('US/Eastern')
    current_date = datetime(2020, 7, 30)
    earliest_date = None
    try:
        with open(FILE_NAME, 'r+') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = []
    except FileNotFoundError:
        print("File not found, creating new file.")
        data = []

    #end_date = current_date #use this to gather the most up-to-date data
    try:
        end_date = datetime.strptime(data[-1]["date"], "%a, %d %b %Y %H:%M:%S %z") #use this to gather historical data
    except IndexError:
        end_date = current_date

    start_date = end_date - timedelta(days=30)

    manager = Manager()
    shared_data = manager.list()
    shared_file = manager.Lock()

    while earliest_date is None or earliest_date > timezone.localize(datetime(1999, 12, 31)):

        print("Getting data for", start_date.strftime("%m/%d/%Y"), "-", end_date.strftime("%m/%d/%Y"))
        page = 1
        while True:
            print("Getting data for", start_date.strftime("%m/%d/%Y"), "-", end_date.strftime("%m/%d/%Y"), "on page", page)
            new_data = get_data(start_date, end_date, page)
            if new_data:
                shared_data.extend(new_data)
                page += 1
                if page > 100:
                    pool = Pool()
                    pool.apply_async(save_data, args=(shared_data, shared_file))
                    pool.close()
                    pool.join()
                    earliest_date = datetime.strptime(shared_data[-1]['date'], "%a, %d %b %Y %H:%M:%S %z")
                    shared_data = manager.list()
                    break
            else:
                pool = Pool()
                pool.apply_async(save_data, args=(shared_data, shared_file))
                pool.close()
                pool.join()
                earliest_date = datetime.strptime(shared_data[-1]['date'], "%a, %d %b %Y %H:%M:%S %z")
                shared_data = manager.list()
                break



        start_date = earliest_date - timedelta(days=30)
        end_date = earliest_date

    print("Finished gathering data.")


if __name__ == '__main__':
    start()