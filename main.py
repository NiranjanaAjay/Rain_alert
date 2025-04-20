import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")

print(api_key)

LAT = "10.107570"
LNG = "76.345665"

parameters = {
    "lat":LAT,
    "lon":LNG,
    "appid":api_key
}

response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
print(data)