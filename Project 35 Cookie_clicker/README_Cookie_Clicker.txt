Cookie Clicker Bot
This Python script automates the Cookie Clicker game using Selenium. It clicks the cookie, checks for available upgrades, and purchases the most expensive affordable upgrade every 5 seconds. The bot runs for 5 minutes and then prints the cookies per second count.

How It Works
The script performs the following tasks:

Opens the Cookie Clicker game using the Selenium WebDriver.
Clicks the cookie continuously.
Checks for available upgrades every 5 seconds.
Purchases the most expensive affordable upgrade.
Prints the cookies per second count after 5 minutes.
Prerequisites
Python 3.x
selenium library
Chrome WebDriver
You can install the required library using:

pip install selenium

Usage
Clone the repository:
git clone https://github.com/UniteUniverse/Python-Programs.git
cd Python-Programs/Project%2035%20Cookie_clicker

Download and install Chrome WebDriver from here and ensure it’s in your PATH.
Run the script:
python cookie_clicker_bot.py

Script Details
chrome_options: Configures the Chrome WebDriver to keep the browser open after the script completes.
cookie: The cookie element to be clicked.
item_ids: List of upgrade item IDs.
cookie_upgrades: Dictionary of store items and prices.
affordable_upgrades: Dictionary of upgrades that can be currently afforded.
Author
Pratyush Kumar Jha
