# 507/206 Homework 6 Part 1
import requests
import sys
from bs4 import BeautifulSoup

#to pick up command line argument
url = sys.argv[1]

#### Part 1 ####
print('\n*********** PART 1 ***********')
print("Mark's page -- Alt tags\n")

### Your Part 1 solution goes here
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

imgs = soup.find_all("img")

for i in imgs:
    if "alt" in i.attrs:
        print(i['alt'])
    else:
        print("No alternative text provided!!")
