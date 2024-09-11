Weather Forecast SMS Notifier
This Python script sends an SMS notification if rain is expected in your area, using the OpenWeatherMap API for weather data and Twilio API for sending SMS.

How It Works
The script performs the following tasks:

Fetches the weather forecast for the next few hours using the OpenWeatherMap API.
Checks if rain is expected by analyzing the weather condition codes.
Sends an SMS notification via Twilio if rain is expected.
Prerequisites
Python 3.x
requests library
twilio library
You can install the required libraries using:

pip install requests twilio

Usage
Clone the repository:
git clone https://github.com/UniteUniverse/Python-Programs.git
cd Python-Programs/Project%2029%20Weather_Forecast

Update the script with your Twilio account SID, auth token, API key, and phone numbers:
Python

account_sid = "your_account_sid"
auth_token = "your_auth_token"
api_key = "your_api_key"
AI-generated code. Review and use carefully. More info on FAQ.
Run the script:
python weather_forecast_notifier.py

Script Details
parameters: Contains the latitude, longitude, API key, and the number of forecast hours.
will_rain: Boolean flag to check if rain is expected.
Twilio SMS: Sends an SMS if rain is expected.
Author
Pratyush Kumar Jha
