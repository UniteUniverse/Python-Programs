Workout Tracker
This Python script tracks your workouts by leveraging natural language processing to extract information about the exercises you did. It uses the Nutritionix API to obtain exercise data based on your input and sends the workout information to a Google Sheets document using the Sheety API.

How It Works
The script performs the following tasks:

Takes user input for the exercise performed.
Fetches exercise data using the Nutritionix API.
Logs the workout data including date, time, exercise, duration, and calories burned to a Google Sheets document using the Sheety API.
Prerequisites
Python 3.x
requests library
You can install the required library using:

pip install requests

Usage
Clone the repository:
git clone https://github.com/UniteUniverse/Python-Programs.git
cd Python-Programs/Project%2032%20Workout_Tracker

Update the script with your API keys and authentication details:
Python

APP_ID = "your_app_id"
API_KEY = "your_api_key"
AI-generated code. Review and use carefully. More info on FAQ.
Run the script:
python workout_tracker.py

Script Details
headers: Contains the content type, app ID, and app key for authentication.
exercise_parameters: Contains the user input for the exercise performed.
workouts: Contains the workout data to be logged.
HTTPBasicAuth: Used for authenticating the request to the Sheety API.
Author
Pratyush Kumar Jha
