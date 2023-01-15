import requests
from datetime import datetime
import math
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

with open("/Users/Cook/Documents/API Keys/Twilio Auth Key.txt") as f:
    AUTH_KEY = f.readline()
    f.close()
with open("/Users/Cook/Documents/API Keys/Phone Number.txt") as f:
    PH_NO = f.readline()
    f.close()


# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC5b619f8419ede2b6b1c586a5f0842dd5"
auth_token = AUTH_KEY
client = Client(account_sid, auth_token)




OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY: str
LAT = 32.779167
LNG = -96.808891
RAIN_IN_24 = False
RAIN_IN_12 = False

today = datetime.today()


with open("/Users/Cook/Documents/API Keys/Open Weather.txt") as f:
    API_KEY = f.readline()
    f.close()


weather_parameters = {

    "lat": LAT,
    "lon": LNG,
    "appid": API_KEY

}

weather_connection = requests.get(OWM_ENDPOINT, params=weather_parameters)
weather_connection.raise_for_status()
weather_connection_json = [weather_connection.json()["list"]]

for idx in range(len(weather_connection_json[0])):
    if 200 <= weather_connection.json()["list"][idx]["weather"][0]["id"] <= 701:
        if idx in range(4):
            RAIN_IN_12 = True
            print(
                "It's going to precipitate within 12 hours, keep an umbrella or raincoat handy")
        elif idx in range(8):
            print(
                "It's going to precipitate within 24 hours, keep an umbrella or raincoat handy")
            RAIN_IN_24 = True

        # dividing by 8 because there are 8 reports per day
        day_as_a_number = datetime.isoweekday(today) + idx/8
        if day_as_a_number > 7:
            day_as_a_number -= 7
        day_as_a_number = math.ceil(day_as_a_number)

        days = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

        day_as_a_name = [days[day]
                         for day in range(len(days)) if day_as_a_number == day+1]

        print(f"\nIt's going to precipitate on {day_as_a_name[0]}")
        how_much_rain = weather_connection.json(
        )["list"][idx]["weather"][0]["description"].title()
        type_of_rain = weather_connection.json(
        )["list"][idx]["weather"][0]["main"].title()
        print(f"It's going to be {type_of_rain}, with {how_much_rain}\n")
        print("Don't forget your umbrella and raincoat that day\n")

if RAIN_IN_12 == True:
    message = client.messages.create(
    body="It's going to rain within 12 hours",
    from_="+19294294840",
    to=PH_NO
)

    print(message.sid)
elif RAIN_IN_24 == True:
    message = client.messages.create(
    body="It's going to rain within 24 hours",
    from_="+19294294840",
    to=PH_NO
)   
    print(message.status)

# print(weather_connection.json()["list"][0]["weather"][0]["main"])
# print(weather_connection.json()["list"][0]["weather"][0]["description"].title())
# print(location_connection.json())
