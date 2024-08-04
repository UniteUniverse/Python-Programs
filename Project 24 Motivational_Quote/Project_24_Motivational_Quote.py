import datetime as dt
from random import*
import smtplib
my_email="t9940472@gmail.com"
password="vbqj xpse uvtk ncmm"
day=dt.datetime.now().weekday()

with open(file="Motivational Quote Project 24\quotes.txt") as quote:
    quote_list=quote.readlines()
    choosen_quote=quote_list[randint(0,len(quote_list))]
if day==1:
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="pratyush.snj@gmail.com",msg=f"Subject:Motivation\n\n{choosen_quote}")
else:
    print("Today is not Monday.")
