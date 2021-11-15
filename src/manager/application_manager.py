from api.game_info_api import GameInfoApi
import web_scraper.gry_online_scraper as scraper


class ApplicationManager:
    title: str
    api: GameInfoApi
    games: list

    def __init__(self):
        self.api = GameInfoApi()
        self.games = self.api.get_games()

    def post_game_title(self, title):
        self.title = title

    def get_game_by_title(self, title):
        if title is None:
            title = self.title

        for game in self.games:
            if game.name.lower() == title.lower():
                game = self.api.get_game_details(game.game_id)
                requirements = scraper.scrape(title)
                game.pc_requirements_minimum = requirements['minimal']
                game.pc_requirements_recommended = requirements['recommended']

                return game
