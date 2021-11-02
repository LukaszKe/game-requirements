from bs4 import BeautifulSoup
from selenium import webdriver
import requests

URL = "https://www.gry-online.pl/gry/diablo-ii-resurrected/z55e65"
page = requests.get(URL)


soup = BeautifulSoup(page.content, 'html.parser')

req_div = soup.find("div", {"id": "game-requirements-cnt-1-c"})

minimal = {
    "cpu": [],
    "ram": "",
    "gpu": []
}

recommended = {
    "cpu": [],
    "ram": "",
    "gpu": []
}

requirements = []

for ultag in req_div.find_all('ul'):
    for litag in ultag.find_all('li'):
        requirements.append(litag.text)

minimal["cpu"] = [req.strip() for req in requirements[1].split('/')]
minimal["ram"] = requirements[2].strip()
minimal["gpu"] = [req.strip() for req in requirements[3][14:-10].split('/')]

if len(requirements) > 6:
    recommended["cpu"] = [req.strip() for req in requirements[7].split('/')]
    recommended["ram"] = requirements[8]
    recommended["gpu"] = [req.strip()
                          for req in requirements[9][14:-10].split('/')]
