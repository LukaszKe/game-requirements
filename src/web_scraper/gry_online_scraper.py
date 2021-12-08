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
    minimal.ram = requirements[2].strip().split()[0]
    if 'MB' in minimal.ram:
        minimal.ram = float(minimal.ram.split('MB')[0]) / 1024
    minimal.gpu = requirements[3][14:-10].split('/')[0].strip()
    minimal.free_space = requirements[4].split('GB')[0]

    if len(requirements) > 6:
        recommended.cpu = requirements[7].split('/')[0].strip()
        recommended.ram = requirements[8].split()[0]
        if 'MB' in recommended.ram:
            recommended.ram = float(minimal.ram.split('MB')[0]) / 1024
        recommended.gpu = requirements[9][14:-10].split('/')[0].strip()
        recommended.free_space = requirements[10].split('GB')[0]
        return {'minimal': minimal, 'recommended': recommended}

    return {'minimal': minimal}
