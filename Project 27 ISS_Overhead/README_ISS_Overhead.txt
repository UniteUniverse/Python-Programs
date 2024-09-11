ISS Overhead Notifier
This Python script notifies you via email when the International Space Station (ISS) is overhead and it’s nighttime at your location.

How It Works
The script performs the following tasks:

Fetches the current position of the ISS using the Open Notify API.
Checks if the ISS is within +5 or -5 degrees of your location.
Fetches the sunrise and sunset times for your location using the Sunrise-Sunset API.
Determines if it is currently nighttime at your location.
Sends an email notification if both conditions are met (ISS is overhead and it’s nighttime).
Prerequisites
Python 3.x
requests library
smtplib library
You can install the required libraries using:

pip install requests

Usage
Clone the repository:
git clone https://github.com/UniteUniverse/Python-Programs.git
cd Python-Programs/Project%2027%20ISS_Overhead

Update the script with your email and password:
Python

my_email = "your_email@example.com"
password = "your_password"
AI-generated code. Review and use carefully. More info on FAQ.
Run the script:
python iss_overhead_notifier.py

Script Details
MY_LAT and MY_LONG: Your geographical coordinates.
iss_overhead(): Checks if the ISS is within +5 or -5 degrees of your location.
is_night(): Checks if it is currently nighttime at your location.
Email Notification: Sends an email if the ISS is overhead and it’s nighttime.
Author
Pratyush Kumar Jha
