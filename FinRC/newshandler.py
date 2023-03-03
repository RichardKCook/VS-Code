# import requests
# import json
# from datetime import datetime, timedelta
# import pytz

# API_KEY = "jjhoo2v1s8ia0s9z8dkik8yoj3vjngv0fwvxepdg"
# API_ENDPOINT = "https://stocknewsapi.com/api/v1/category"
# FILE_NAME = "stock_news.json"

# def get_data(start_date, end_date, page):
#     data = []
#     params = {
#         "section": "alltickers",
#         "items": 100,
#         "page": page,
#         "date": start_date.strftime("%m%d%Y") + "-" + end_date.strftime("%m%d%Y"),
#         "token": API_KEY
#     }
#     response = requests.get(API_ENDPOINT, params=params)
#     if response.status_code == 200:
#         json_data = response.json()
#         if not json_data['data']:
#             return None
#         for item in json_data['data']:
#             data.append({
#                 "date": item["date"],
#                 "sentiment": item["sentiment"],
#                 "tickers": item["tickers"]
#             })
#         return data
#     else:
#         print("Error:", response.status_code)
#         return None

# def start():
#     timezone = pytz.timezone('US/Eastern')
#     current_date = datetime.now(timezone)
#     earliest_date = None
#     try:
#         with open(FILE_NAME, 'r+') as f:
#             try:
#                 data = json.load(f)
#             except json.decoder.JSONDecodeError:
#                 data = []
#     except FileNotFoundError:
#         print("File not found, creating new file.")
#         data = []

#     end_date = current_date
#     start_date = end_date - timedelta(days=30)

#     while earliest_date is None or earliest_date > timezone.localize(datetime(1999, 12, 31)):
        
#         print("Getting data for", start_date.strftime("%m/%d/%Y"), "-", end_date.strftime("%m/%d/%Y"))
#         page = 1
#         while True:
#             print("gathering data for ", start_date.strftime("%m/%d/%Y"), " to ", end_date.strftime("%m/%d/%Y"), " on page ", page)
#             new_data = get_data(start_date, end_date, page)
#             if new_data:
#                 data.extend(new_data)
#                 page += 1
#                 if page > 100:
#                     earliest_date = datetime.strptime(data[-1]['date'], "%a, %d %b %Y %H:%M:%S %z")
#                     break
#             else:
#                 break
#         start_date = earliest_date - timedelta(days=30)
#         end_date = earliest_date
#     with open(FILE_NAME, 'w') as f:
#         json.dump(data, f, indent=4)
#     print("Finished gathering data.")

# start()


import requests
import json
from datetime import datetime, timedelta
import pytz
from time import sleep

API_KEY = "jjhoo2v1s8ia0s9z8dkik8yoj3vjngv0fwvxepdg"
API_ENDPOINT = "https://stocknewsapi.com/api/v1/category"
FILE_NAME = "stock_news.json"
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


def save_data(data):
    print("Saving data...")
    try:
        with open(FILE_NAME, 'r') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = []

    # Find new data
    new_data = []
    global FIRST_SAVE
    if FIRST_SAVE:
        for d in data:
            if d not in existing_data:
                new_data.extend(d)
        FIRST_SAVE = False
    else:
        for d in data:
            if d not in existing_data[-100:]:
                new_data.extend(d)

    # Update data
    existing_data.extend(new_data)

    # Save data
    with open(FILE_NAME, 'w') as f:
        json.dump(existing_data, f, indent=4)

    data = []


def start():
    timezone = pytz.timezone('US/Eastern')
    current_date = datetime.now(timezone)
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
        end_date = datetime.strptime(data[-1]["date"], "%a, %d %b %Y %H:%M:%S %z") - timedelta(days=1) #use this to gather historical data
    except IndexError:
        end_date = current_date

    start_date = end_date - timedelta(days=30)

    while earliest_date is None or earliest_date > timezone.localize(datetime(1999, 12, 31)):
       
        print("Getting data for", start_date.strftime("%m/%d/%Y"), "-", end_date.strftime("%m/%d/%Y"))
        page = 1
        while True:
            print("Getting data for", start_date.strftime("%m/%d/%Y"), "-", end_date.strftime("%m/%d/%Y"), "on page", page)
            new_data = get_data(start_date, end_date, page)
            if new_data:
                data.extend(new_data)
                save_data(new_data)  # Save new data
                page += 1
                if page > 100:
                    earliest_date = datetime.strptime(data[-1]['date'], "%a, %d %b %Y %H:%M:%S %z")
                    break
            else:
                break
        start_date = earliest_date - timedelta(days=30)
        end_date = earliest_date - timedelta(days=1)

    # save_data(data)  # Save final data
    print("Finished gathering data.")


start()