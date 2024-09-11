import requests
import datetime as dt
import math
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid=""#Enter your own from twilio site
auth_token=""#Enter your own from twilio site

api_key_stock=""#Enter your own from stock api site alphavantage
api_key_news=""#Enter your own from newsapi.org
parameters_stock={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":api_key_stock
}
date_today=dt.datetime.now()
day=date_today.day-2
month=date_today.month
year=date_today.year
if int(day)//10==0 and int(month)//10==0:
    analysis_date=str(year)+'-0'+str(month)+'-0'+str(day)
elif int(day)//10==0:
    analysis_date=str(year)+'-'+str(month)+'-0'+str(day)
elif int(month)//10==0:
    analysis_date=str(year)+'-0'+str(month)+'-'+str(day)
else:
    analysis_date=str(year)+'-'+str(month)+'-'+str(day)
response=requests.get("https://www.alphavantage.co/query",params=parameters_stock)
response.raise_for_status
data_stock=response.json()
daily_data=data_stock["Time Series (Daily)"][analysis_date]
opening_price=1000
closing_price=500
difference_in_price=closing_price-opening_price
percentage_of_fluctuation=round((difference_in_price/opening_price)*100,1)
parameters_news={
    "q":"tesla",
    "from":analysis_date,
    "sortBy":"publishedAt",
    "apiKey":api_key_news
}
response2=requests.get("https://newsapi.org/v2/everything",params=parameters_news)
data_news=response2.json()
news_data_headline=data_news["articles"][0]["title"]
news_data_brief=data_news["articles"][0]["description"]


if percentage_of_fluctuation<=-5 or percentage_of_fluctuation>=5:
    if percentage_of_fluctuation<=-5:
        client=Client(account_sid,auth_token)
        message=client.messages.create(
                body=f"{STOCK} 🔻{percentage_of_fluctuation*-1}%\nHeadline: {news_data_headline}?\nBrief: {news_data_brief}.",
                from_="+12296964330",
                to="",#Enter your number to receive message.
            )
    else:
        client=Client(account_sid,auth_token)
        message=client.messages.create(
            body=f"{STOCK} 🔺{percentage_of_fluctuation}%\nHeadline: {news_data_headline}?\nBrief: {news_data_brief}.",
            from_="+12296964330",
            to="",#Enter your number to receive message.
        )

