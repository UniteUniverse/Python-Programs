import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response=requests.get(url=URL)
movies_webpage=response.text
soup=BeautifulSoup(movies_webpage, "html.parser")
title_list=soup.find_all(name="h3", class_="title")
reverse_title_list=title_list[::-1]
for i in range(0,len(reverse_title_list)):
    with open("movies.txt","a", encoding="utf-8") as file:
        file.write(reverse_title_list[i].getText()+"\n") 
