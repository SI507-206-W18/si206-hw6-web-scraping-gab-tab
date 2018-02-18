# 507/206 Homework 6 Extra Credit 1
import requests
from bs4 import BeautifulSoup

#### Extra Credit 2 ####
print('\n*********** EXTRA CREDIT 2 ***********')
print('Re-sort Atheletes by State\n')

### Your Extra Credit 2 solution goes here
html = requests.get("https://www.athletic.net/CrossCountry/Results/Meet.aspx?Meet=135827").text
soup = BeautifulSoup(html, 'html.parser')

runners = soup.find("tbody", id= "D_557666")
all_runners = runners.find_all("tr", class_ = "official")

list_of_runners = []
for runner in all_runners:
    runner_name = runner.find("a", class_ = "aN").text
    team = runner.find_all('td')[5].text
    if "MI" in team:
        list_of_runners.append(runner_name)

print("Top 3 Men for Michigan:")
finish_count = 1
for mi_run in list_of_runners[:3]:
    print("{}. {}".format(finish_count, mi_run))
    finish_count += 1

female_runners = soup.find("tbody", id= "D_557668")
all_runners = female_runners.find_all("tr", class_ = "official")

list_of_runners = []
for runner in all_runners:
    runner_name = runner.find("a", class_ = "aN")
    if runner_name:
        runner_name = runner_name.text
    team = runner.find_all('td')[5].text
    if "MI" in team:
        list_of_runners.append(runner_name)

print("Top 3 Women for Michigan:")
finish_count = 1
for mi_run in list_of_runners[:3]:
    print("{}. {}".format(finish_count, mi_run))
    finish_count += 1
