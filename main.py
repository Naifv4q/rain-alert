import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(dotenv_path="C:/Projects/Enviromental Variables/Python/rain-alert-env/config.env")


#Open Weather API Info:
api_key = os.getenv("OWM_API_KEY")
OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

MY_LAT = 21.251385
MY_LNG = 81.629639
FROM_WHTSP_NUM = os.getenv("MY_TWILIO_NUM")
TO_WHTSP_NUM = os.getenv("MY_NUM")

#Twilio info
my_acc_sid = os.getenv("ACC_SID")
my_auth_token = os.getenv("AUTH_TOKEN")

client = Client(my_acc_sid,my_auth_token)



param = {
    "lat":MY_LAT,
    "lon":MY_LNG,
    "appid": api_key,
    "cnt" : 4,
}

response = requests.get(url=OMW_ENDPOINT,params=param)
response.raise_for_status()

will_rain = False
weather_data = response.json()
for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700: # type: ignore
        will_rain = True
   
if will_rain == True:
    message = client.messages.create(
        body="بتمطر اليوم بإذن الله 🌧️",
        from_=FROM_WHTSP_NUM,
        to= TO_WHTSP_NUM # type: ignore
    )
    print(message.status)


