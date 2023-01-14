import requests
import gmplot


with open("/Users/Cook/Documents/API Keys/gMaps API.txt", mode="r") as f:
    api_key = f.read()
    f.close


response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

iss_latitude = float(response.json()["iss_position"]["latitude"])
iss_longitude = float(response.json()["iss_position"]["longitude"])


gmap = gmplot.GoogleMapPlotter(iss_latitude, iss_longitude, 5, apikey=api_key)
gmap.marker(iss_latitude, iss_longitude)


gmap.draw("Current ISS Location.html")
