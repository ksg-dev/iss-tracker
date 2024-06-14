import requests
from datetime import datetime
import math

MY_LAT = 30.673290
MY_LONG = -88.111153

# to see dict in browser: https://api.sunrise-sunset.org/json?lat=30.673290&lng=-88.111153&formatted=0

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

print(iss_latitude, iss_longitude)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()



def is_close(iss_lat, iss_long):
    # check if close to my location
    if math.isclose(iss_lat, MY_LAT, abs_tol=5) and math.isclose(iss_long, MY_LONG, abs_tol=5):
        return True
    else:
        return False

def is_dark():
    # print(sunset, time_now.hour, sunrise)
    if sunset < time_now.hour < sunrise:
        return True
    else:
        return False

def main():
    # If the ISS is close to my current position
    if is_close(iss_latitude, iss_longitude):
        # and it is currently dark
        if is_dark():
        # send me an email to tell me to look up.
        # BONUS: run the code every 60 seconds.

print(is_dark())



