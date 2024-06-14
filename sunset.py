import requests
from datetime import datetime

MY_LAT = 30.673290
MY_LONG = -88.111153

# to see dict in browser: https://api.sunrise-sunset.org/json?lat=30.673290&lng=-88.111153

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# format to only get hours in format of 24 hour clock
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]



print(sunrise)
print(sunset)

# time_now = datetime.now()
# print(time_now)
