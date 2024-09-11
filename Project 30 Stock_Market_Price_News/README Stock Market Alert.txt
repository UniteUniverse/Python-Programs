Stock Market Price and News Notifier
This Python script sends an SMS notification if there is a significant fluctuation in the stock price of Tesla Inc. (TSLA) and provides the latest news headline and brief related to the company.

How It Works
The script performs the following tasks:

Fetches the daily stock price data for Tesla Inc. (TSLA) using the Alpha Vantage API.
Calculates the percentage fluctuation in the stock price.
Fetches the latest news related to Tesla Inc. using the News API.
Sends an SMS notification via Twilio if the stock price fluctuation is greater than or equal to 5%.
Prerequisites
Python 3.x
requests library
twilio library
You can install the required libraries using:

pip install requests twilio

Usage
Clone the repository:
git clone https://github.com/UniteUniverse/Python-Programs.git
cd Python-Programs/Project%2030%20Stock_Market_Price_News

Update the script with your Twilio account SID, auth token, API keys, and phone numbers:
Python

account_sid = "your_account_sid"
auth_token = "your_auth_token"
api_key_stock = "your_api_key_stock"
api_key_news = "your_api_key_news"
AI-generated code. Review and use carefully. More info on FAQ.
Run the script:
python stock_market_price_news_notifier.py

Script Details
STOCK: The stock symbol for Tesla Inc. (TSLA).
parameters_stock: Contains the function, symbol, and API key for fetching stock data.
parameters_news: Contains the query, date, sort order, and API key for fetching news data.
percentage_of_fluctuation: Calculates the percentage change in stock price.
Twilio SMS: Sends an SMS if the stock price fluctuation is greater than or equal to 5%.
Author
Pratyush Kumar Jha
