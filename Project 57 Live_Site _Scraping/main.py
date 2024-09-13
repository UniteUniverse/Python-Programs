from bs4 import BeautifulSoup
import requests
response=requests.get(url="https://news.ycombinator.com/news")
yc_webpage=response.text
soup=BeautifulSoup(yc_webpage, "html.parser")
anchor=soup.find_all(name="span", class_="titleline")
article_text=[]
article_links=[]
article_score=[]
for tag in anchor:
    article=tag.find(name="a")
    title_anchor=article.getText()
    link_anchor=article.get("href")
    article_text.append(title_anchor)
    article_links.append(link_anchor)
score_anchor=soup.find_all(name="span", class_="score")
for score in score_anchor:
    article_score.append(int(score.getText().split(" ")[0]))
index_max_score=article_score.index(max(article_score))
print(article_text[index_max_score], article_links[index_max_score], article_score[index_max_score])
