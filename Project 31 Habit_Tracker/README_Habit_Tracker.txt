Habit Tracker
This Python script interacts with the Pixela API to create and manage a habit tracking graph. It allows you to create a user, set up a graph, add data to the graph, update data, and delete data points.

How It Works
The script performs the following tasks:

Creates a user on Pixela.
Creates a graph for tracking a specific habit.
Adds data points to the graph.
Updates existing data points on the graph.
Deletes data points from the graph.
Prerequisites
Python 3.x
requests library
You can install the required library using:

pip install requests

Usage
Clone the repository:
git clone https://github.com/UniteUniverse/Python-Programs.git
cd Python-Programs/Project%2031%20Habit_Tracker

Update the script with your Pixela username and token:
Python

Username = "your_username"
TOKEN = "your_token"
AI-generated code. Review and use carefully. More info on FAQ.
Run the script:
python habit_tracker.py

Script Details
pixela_endpoint: The base URL for the Pixela API.
user_parameters: Contains the token, username, and agreement to terms of service.
graph_endpoint: The endpoint for creating and managing graphs.
pixel_endpoint: The endpoint for adding, updating, and deleting data points.
headers: Contains the user token for authentication.
Author
Pratyush Kumar Jha
