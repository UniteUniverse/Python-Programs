LinkedIn Job Application Automation
This project automates the process of applying for jobs on LinkedIn using Selenium. It navigates to the LinkedIn job search page, logs in with your credentials, and applies for a specified job.

Table of Contents
Introduction
Prerequisites
Installation
Usage
Author
Introduction
This script automates the job application process on LinkedIn. It logs into your LinkedIn account, navigates to a job listing, and fills out the application form. This can save you time and effort in your job search.

Prerequisites
Before you begin, ensure you have met the following requirements:

Python installed on your system.
Selenium library installed. You can install it using pip:
pip install selenium

ChromeDriver installed and the path to the executable set correctly in the script.
A LinkedIn account with your email and password.
Installation
Clone this repository to your local machine:
git clone https://github.com/UniteUniverse/Python-Programs.git

Navigate to the project directory:
cd Python-Programs/Project%2036%20Linkedin_Jobs_Apply

Install the required libraries:
pip install selenium

Usage
Open the script file and update the following variables with your LinkedIn credentials:
Python

email.send_keys("your_email")  # Enter Your Email
password.send_keys("your_password")  # Enter Your Password
AI-generated code. Review and use carefully. More info on FAQ.
Run the script:
python linkedin_job_apply.py

The script will open a Chrome browser, navigate to the LinkedIn job search page, log in to your account, and apply for the job.
Author
Pratyush Kumar Jha
