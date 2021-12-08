import copy
import re

from api.game_info_api import GameInfoApi
import hardware.hardware_reader as hardware_reader
from model.components import Components
import web_scraper.gry_online_scraper as scraper
from model.game import Game
from database.database_manager import DatabaseManager


class ApplicationManager:
    game: Game
    api: GameInfoApi
    games: list
    user_components: Components
    database_manager: DatabaseManager

    def __init__(self):
        self.api = GameInfoApi()
        self.games = self.api.get_games()
        self.user_components = hardware_reader.get_components()
        self.database_manager = DatabaseManager()

    def post_game_title(self, title):
        self.game = self.get_game_by_title(title)

    def get_game_by_title(self, title):
        if title is None:
            return self.game

        title = title.lower().strip()
        for game in self.games:
            if game.name.lower() == title:
                self.game = self.check_requirements(game)
                return self.game

    def check_requirements(self, game):
        requirements = scraper.scrape(game.name)
        game = self.api.get_game_details(game.game_id)

        game.pc_requirements_minimum = requirements['minimal']
        game.runs = self.compare_requirements(game.pc_requirements_minimum)

        if 'recommended' in requirements:
            game.pc_requirements_recommended = requirements['recommended']
            self.compare_requirements(game.pc_requirements_recommended)

        return game

    def compare_requirements(self, requirements):
        runs = True
        print(vars(requirements))
        print(vars(self.user_components))

        try:  # comparing gpu
            if requirements.gpu:
                user_gpu = self.database_manager.get_gpu_by_name(self.user_components.gpu)
                required_gpu = self.database_manager.get_gpu_by_name(' '.join(requirements.gpu.split()[2:]))
                requirements.gpu_ok = user_gpu.gpu_mark >= required_gpu.gpu_mark
                if runs is not None:
                    runs = runs and requirements.gpu_ok
            else:
                requirements.gpu_ok = True
        except Exception as ex:
            print(ex)
            runs = None

        try:  # comparing cpu
            if requirements.cpu:
                user_cpu_name = parse_cpu_name(self.user_components.cpu)
                user_cpu = self.database_manager.get_cpu_by_name_in(user_cpu_name)
                required_cpu_name = parse_cpu_name(requirements.cpu)
                required_cpu = self.database_manager.get_cpu_by_name_in(required_cpu_name)
                requirements.cpu_ok = user_cpu.cpu_mark >= required_cpu.cpu_mark
                if runs is not None:
                    runs = runs and requirements.cpu_ok
            else:
                requirements.cpu_ok = True
        except Exception as ex:
            print(ex)
            runs = None

        try:  # comparing ram
            requirements.ram_ok = self.user_components.ram >= float(requirements.ram)
            if runs is not None:
                runs = runs and requirements.ram_ok
        except Exception as ex:
            print(ex)
            runs = None

        try:  # comparing disk space
            requirements.free_space_ok = self.user_components.free_space >= float(requirements.free_space)
            if runs is not None:
                runs = runs and requirements.free_space_ok
        except Exception as ex:
            print(ex)
            runs = None

        return runs


def parse_cpu_name(name: str):
    if name.startswith('Intel'):
        regex = re.compile("[^\\s]*\\d{4}[^\\s]*")
        found = regex.search(name)
        if found:
            return found.group()
    return name
