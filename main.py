import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
api_key = os.getenv("api_key")

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)
print(client)


LAT = "10.107570"
LNG = "76.345665"

parameters = {
    "lat":LAT,
    "lon":LNG,
    "appid":api_key,
    "cnt":4
}

response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for i in range(4):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    if int(weather_id)<700:
        will_rain = True
if will_rain:
    print("It will rain")