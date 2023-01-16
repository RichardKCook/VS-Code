import requests
from datetime import datetime
from datetime import timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
with open("/Users/Cook/Documents/API Keys/Alphavantage API.txt") as f:
    AV_API = f.readline()
    f.close()
with open("/Users/Cook/Documents/API Keys/newsapi.txt") as f:
    NEWS_API = f.readline()
    f.close
with open("/Users/Cook/Documents/API Keys/Phone Number.txt") as f:
    PH_NO = f.readline()
    f.close()
with open("/Users/Cook/Documents/API Keys/Twilio Auth Key.txt") as f:
    AUTH_KEY = f.readline()
    f.close()

account_sid = "AC5b619f8419ede2b6b1c586a5f0842dd5"
auth_token = AUTH_KEY
client = Client(account_sid, auth_token)

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": AV_API

}
news_parameters = {

    "q": COMPANY_NAME,
    "pagesize": 3,
    "category": "business",
    "country": "us",
    "apiKey": NEWS_API
}


day_as_a_number = datetime.isoweekday(datetime.today())

day_as_a_name = [days[day]
                 for day in range(len(days)) if day_as_a_number == day+1]


stock_response = requests.get(
    f"https://www.alphavantage.co/query?", params=stock_parameters)
stock_response.raise_for_status()
for i in range(3, 4):
    soonest_date = str(datetime.today()-timedelta(days=i)).split(" ")[0]
    second_soonest_date = str(
        datetime.today()-timedelta(days=i+1)).split(" ")[0]
    try:
        closing_price_1 = float(stock_response.json(
        )["Time Series (Daily)"][f"{soonest_date}"]["4. close"])
        closing_price_2 = float(stock_response.json(
        )["Time Series (Daily)"][f"{second_soonest_date}"]["4. close"])
    except KeyError:
        pass
    percent_change = ((closing_price_1-closing_price_2)/closing_price_1)*100
    if (percent_change > 5) or percent_change < -5:

        headlines = []
        bodies = []
        urls = []
        news_response = requests.get(
            "https://newsapi.org/v2/top-headlines?", params=news_parameters)

        for i in range(0, 1):
            try:
                headlines.append(news_response.json()["articles"][i]["title"])
                bodies.append(news_response.json()[
                              "articles"][i]["description"])
                urls.append(news_response.json()["articles"][i]["url"])

            except IndexError:
                print("No Recent Articles Found")
            percent_change_in_2_decimals = "{:.2f}".format(percent_change)
            if percent_change > 5:
                message = client.messages.create(
                    body=f"{COMPANY_NAME}: 🔺{percent_change_in_2_decimals}%\nHeadline: {headlines[0]}\nBrief: {bodies[0]}\nLink: {urls[0]}",
                    from_="+19294294840",
                    to=PH_NO
                )
                print(message.status)

            elif percent_change < -5:
                message = client.messages.create(
                    body=f"{COMPANY_NAME}: 🔻{percent_change_in_2_decimals}%\nHeadline: {headlines[0]}\nBrief: {bodies[0]}\nLink: {urls[0]}",
                    from_="+19294294840",
                    to=PH_NO
                )

