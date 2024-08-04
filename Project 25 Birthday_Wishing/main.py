from pandas import *
import datetime as dt
from random import*
import smtplib
my_email="t9940472@gmail.com"
password="vbqj xpse uvtk ncmm"
data=read_csv(r"Project 25 Birthday Wishing\birthdays.csv")
current_day=dt.datetime.now().day
current_month=dt.datetime.now().month
data_dic=data.to_dict(orient="records")
names=[]
email=[]
n=0
for _ in range(len(data_dic)):
    if data_dic[_]["month"]==current_month and data_dic[_]["day"]==current_day:
        names.append(data_dic[_]["name"])
        email.append(data_dic[_]["email"])
with open(fr"Project 25 Birthday Wishing\letter_templates\letter_{randint(1,3)}.txt")as letter_file:
     letter_contents=letter_file.read()
for name in names:
     stripped_name=name.strip()
     new_letter=letter_contents.replace("[NAME]", stripped_name)
     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email[n],msg=f"Subject:God Bless You\n\n{new_letter}")
     n+=1