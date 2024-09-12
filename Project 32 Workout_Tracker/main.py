import requests
import datetime as dt
from requests.auth import HTTPBasicAuth
today_date=dt.datetime.now()
APP_ID=""#Use Your Own
API_KEY=""Use Your Own
headers={
    "Content-Type": 'application/json',
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}
user_input=input("Tell me which exercise you did: ")
exercise_parameters={
    "query":user_input
}
response=requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",json=exercise_parameters,headers=headers)
response.raise_for_status
response=response.json()
print(response["exercises"][0]["user_input"])
workouts={"workout":{
    "date":today_date.strftime("%d/%m/%Y"),
    "time":today_date.strftime("%H:%M:%S"),
    "exercise":response["exercises"][0]["user_input"],
    "duration":response["exercises"][0]["duration_min"],
    "calories":response["exercises"][0]["nf_calories"],
}}
basic = HTTPBasicAuth('#Username', '#Password') #Add your own from Sheety
response_sheet=requests.post(url="https://api.sheety.co/bcd84812db56f5df7e75f8b9dfce4e98/myWorkouts/workouts",json=workouts,auth=basic)
response_sheet.raise_for_status
print(response_sheet.text)
