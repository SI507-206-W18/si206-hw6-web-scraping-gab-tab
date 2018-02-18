# 507/206 Homework 6 Extra Credit 1
import requests
from bs4 import BeautifulSoup

#### Extra Credit 1 ####
print('\n*********** EXTRA CREDIT 1 ***********')
print('Top Headlines\n')

### Your Extra Credit 1 solution goes here
html = requests.get("https://www.michigandaily.com/section/news").text
soup = BeautifulSoup(html, 'html.parser')

top_10_news = soup.find_all("div", class_= "views-field views-field-field-short-headline")[:10]

print("Top 10 Headlines: news")
for x in top_10_news:
    print(x.text)

html = requests.get("https://www.michigandaily.com/section/sports").text
soup = BeautifulSoup(html, 'html.parser')

top_10_sports = soup.find_all("div", class_= "views-field views-field-field-short-headline")[:10]

print("\nTop 10 Headlines: sports")
for x in top_10_sports:
    print(x.text)

html = requests.get("https://www.michigandaily.com/section/arts").text
soup = BeautifulSoup(html, 'html.parser')

top_10_arts= soup.find_all("div", class_= "views-field views-field-field-short-headline")[:10]

print("\nTop 10 Headlines: arts")
for x in top_10_arts:
    print(x.text)
