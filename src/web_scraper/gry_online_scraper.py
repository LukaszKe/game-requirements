from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from googlesearch import search


def scrape(game_title):
    URLs = search('gry-online.pl' + ' ' +
                  game_title, tld="pl", lang="pl", num=10)
    URL = next(URLs)
    while not "gry-online" in URL:
        URL = next(URLs)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    req_div = soup.find("div", {"id": "game-requirements-cnt-1-c"})

    minimal = {
        "cpu": [],
        "ram": "",
        "gpu": [],
        "space": ""
    }

    recommended = {
        "cpu": [],
        "ram": "",
        "gpu": [],
        "space": ""
    }

    requirements = []

    for ultag in req_div.find_all('ul'):
        for litag in ultag.find_all('li'):
            requirements.append(litag.text)

    minimal["cpu"] = [req.strip() for req in requirements[1].split('/')]
    minimal["ram"] = requirements[2].strip()
    minimal["gpu"] = [req.strip()
                      for req in requirements[3][14:-10].split('/')]

    if len(requirements) > 6:
        recommended["cpu"] = [req.strip()
                              for req in requirements[7].split('/')]
        recommended["ram"] = requirements[8]
        recommended["gpu"] = [req.strip()
                              for req in requirements[9][14:-10].split('/')]

    return {'minimal': minimal, 'recommended': recommended}
