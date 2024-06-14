import requests
from datetime import datetime
import math
import smtplib
import time


MY_LAT = 30.673290
MY_LONG = -88.111153
EMAIL_CONTENT = "The ISS is above you in the sky!"

# to see dict in browser: https://api.sunrise-sunset.org/json?lat=30.673290&lng=-88.111153&formatted=0

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


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
    # Your position is within +5 or -5 degrees of the ISS position.
    if math.isclose(iss_lat, MY_LAT, abs_tol=5) and math.isclose(iss_long, MY_LONG, abs_tol=5):
        return True
    else:
        return False


def send_email(email_content):
    my_email = "testemail.ksg.data@gmail.com"
    app_password = "tjfe xxdk yojh xpuc"
    to_email = "testemailksg.data@yahoo.com"
    subject = "Look Up!"
    body = email_content

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject: {subject} \n\n{body}"
        )


def is_dark():
    # print(sunset, time_now.hour, sunrise)
    if sunset <= time_now.hour <= sunrise:
        return True
    else:
        return False


# BONUS: run the code every 60 seconds.
time.sleep(60)
while True:
    # If the ISS is close to my current position
    if is_close(iss_latitude, iss_longitude):
        # and it is currently dark
        if is_dark():
            # send me email to tell me to look up.
            send_email(EMAIL_CONTENT)



