from bs4 import BeautifulSoup
import requests
from googlesearch import search

from model.components import Components


def scrape(game_title):
    urls = search('gry-online.pl' + ' ' +
                  game_title, tld="pl", lang="pl", num=10)
    url = next(urls)
    while "gry-online" not in url:
        url = next(urls)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    req_div = soup.find("div", {"id": "game-requirements-cnt-1-c"})

    minimal = Components()
    recommended = Components()

    requirements = []

    for ul_tag in req_div.find_all('ul'):
        for li_tag in ul_tag.find_all('li'):
            requirements.append(li_tag.text)

    minimal.cpu = requirements[1].split('/')[0].strip()
    minimal.ram = requirements[2].strip()
    minimal.gpu = requirements[3][14:-10].split('/')[0].strp()

    if len(requirements) > 6:
        recommended.cpu = requirements[7].split('/')[0].strip()
        recommended.ram = requirements[8]
        recommended.gpu = requirements[9][14:-10].split('/')[0].strip()

    return {'minimal': minimal, 'recommended': recommended}
