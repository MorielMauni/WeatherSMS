import requests
from twilio.rest import Client

# https://openweathermap.org/api
api_key = "<API Key>"
weather_website = "https://api.openweathermap.org/data/2.5/forecast"

# https://www.twilio.com/
account_sid = "<Account_SID>"
auth_token = "<Auth_token>"

def client_message():
    """ The function that sends the SMS"""
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Hi <User_Name> \nThe weather today going to be {weather_type}",
        from_="<Phone_Number>",
        to="<Phone_Number_2>"
    )
    print(message.status)

weather_parameter = {
    "appid": api_key,
    "lat": "<Lat>",
    "lon": "<Lon>",
    "cnt": 4,
}

responed = requests.get(weather_website, params=weather_parameter)
responed.raise_for_status()
weather_data = responed.json()
for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    weather_type = hour_data["weather"][0]["main"]
    if weather_id > 800:
        client_message()
    elif weather_id == 800:
        client_message()
    elif 500 >= weather_id <= 531:
        client_message()
