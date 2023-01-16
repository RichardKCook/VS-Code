import requests
from datetime import datetime
NUM_OF_CUPS = 2


PIXELA_ENDPOINT = "https://pixe.la/v1/users/"


with open("/Users/Cook/Documents/API Keys/pixela_token.txt") as f:
    PIXELA_TOKEN = f.readline()
    f.close()


USERNAME = "richardkcook"

pixela_parameters = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# creates account
# pixela_post = requests.post(PIXELA_ENDPOINT, json=pixela_parameters)
# pixela_post.raise_for_status()

# print(pixela_post.text)


GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}{USERNAME}/graphs"

GRAPH_CONFIG = {
    "id": "graph1",
    "name": "Coffee Graph",
    "unit": "cups",
    "type": "int",
    "color": "ajisai"
}

HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
# creates graph
# requests.post(GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)
today = datetime.today()

date_as_string = today.strftime("%Y%m%d")

PUSH_CONFIG = {
    "date": date_as_string,
    "quantity": str(NUM_OF_CUPS)

}


pixela_post = requests.post(
    f"{PIXELA_ENDPOINT}{USERNAME}/graphs/graph1", json=PUSH_CONFIG, headers=HEADERS)
print(pixela_post.text)

# pixela_put = requests.put(
#     f"{PIXELA_ENDPOINT}{USERNAME}/graphs/graph1/{date_as_string}", json=PUSH_CONFIG, headers=HEADERS)
# print(pixela_put.text)


# pixela_delete = requests.delete(
#     f"{PIXELA_ENDPOINT}{USERNAME}/graphs/graph1/{date_as_string}", headers=HEADERS)
# print(pixela_delete.text)
