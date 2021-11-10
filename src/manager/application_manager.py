from api.requirment_api_communication import RequirementsApiCommunication


class ApplicationManager:
    title: str
    api: RequirementsApiCommunication
    games: list

    def post_game_title(self, title):
        self.title = title
        self.api = RequirementsApiCommunication()
        self.games = self.api.get_games()

    def get_game_title(self, title):
        if title is None:
            title = self.title

        for game in self.games:
            if game.name == title:
                return self.api.get_game_details(game.game_id)
