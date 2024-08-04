import requests
from twilio.rest import Client
account_sid=""#Enter your account_sid from twilio
auth_token=""#Enter your token from twilio
api_key="" #Enter your API Key
parameters={
    "lat":28.613939,
    "lon":77.209023,
    "appid":api_key,
    "cnt":4
}
response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status
weather_data=response.json()
will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    client=Client(account_sid,auth_token)
    message=client.messages.create(
            body="It's going to rain today. Remember to bring an ☂️",
            from_="+12296964330",
            to="Enter your number",#Enter your number to receive message.
        )
    print(message.status)
    