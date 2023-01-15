import requests
# import gmplot
from datetime import datetime
import folium
import time


MY_LAT = 32.779167
MY_LNG = -96.808891

with open("/Users/Cook/Documents/API Keys/Open Weather.txt", mode="r") as f:
    API_KEY = f.readline()
    f.close

def get_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()

    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])
    return iss_latitude,iss_longitude


# gmap = gmplot.GoogleMapPlotter(iss_latitude, iss_longitude, 5, apikey=api_key)
# gmap.marker(iss_latitude, iss_longitude)


# gmap.draw("Current ISS Location.html")

def main():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    sun_response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()

    data = sun_response.json()

    sunrise_time = data["results"]["sunrise"]
    sunset_time = data["results"]["sunset"]

    just_sunrise_hour = int(sunrise_time.split("T")[1].split(":")[0])-6
    just_sunset_hour = int(sunset_time.split("T")[1].split(":")[0])-6

    time_now = datetime.now()
    
    while True:
        

        iss_latitude = get_iss_location()[0]
        iss_longitude = get_iss_location()[1]
        iss_location = location_connection = requests.get(f"http://api.openweathermap.org/geo/1.0/reverse?lat={iss_latitude}&lon={iss_longitude}&limit=5&appid={API_KEY}")
        location_connection.raise_for_status()

        map1 = folium.Map(location=[iss_latitude, iss_longitude],
                        zoom_start=12, tites="cartodbposition")

        map1 # for use with Jupyter
        try:
            city = iss_location.json()[0]["local_names"]["en"]
        except KeyError: 
            city = None
        except TypeError:
            city= None
        except IndexError:
            pass
        try:
            country = iss_location.json()[0]["country"]
        except TypeError:
            country = None
        except IndexError:
            pass

        if (time_now.hour > just_sunset_hour or time_now.hour < just_sunrise_hour) and (MY_LAT - 10 <= iss_latitude <= MY_LAT + 10 and MY_LNG - 10 <= iss_longitude <= MY_LNG + 10):

            print(datetime.now(),"The ISS is visable")

        elif iss_location.json() == []:
            print(datetime.now(),"Sorry, the ISS is not visible, it is over the ocean")
        else:
            if country == None:
                print(datetime.now(),f"Sorry, the ISS is not visible, it is over {city}")
            elif city == None:
                print(datetime.now(),f"Sorry, the ISS is not visible, it is over {country}")
            else:
                print(datetime.now(),f"Sorry, the ISS is not visible, it is over {city}, {country}")
        
        time.sleep(2)

main()