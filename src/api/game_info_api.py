import requests

from model.game_item import GameItem
from model.game import Game


class GameInfoApi:
    LIST_URL = 'http://api.steampowered.com/ISteamApps/GetAppList/v0001'
    DETAILS = 'http://store.steampowered.com/api/appdetails?appids='

    def get_games(self):
        response = requests.get(self.LIST_URL)
        data = response.json()
        data = data["applist"]["apps"]['app']

        games = []
        for game in data:
            games.append(GameItem(game['appid'], game['name']))
        return games

    def get_game_details(self, game_id):
        response = requests.get(self.DETAILS + str(game_id))
        data = response.json()
        data = data[str(game_id)]['data']

        game = Game()
        game.name = data['name']
        game.is_free = data['is_free']
        game.short_description = data['short_description']
        game.header_image = data['header_image']

        game.publishers = data['publishers']
        if 'price_overview' in data:
            game.price = data['price_overview']['final_formatted']
        game.categories = data['genres']
        game.release_date = data['release_date']['date']

        if 'metacritic' in data:
            game.metacritic_score = data['metacritic']['score']

        return game
