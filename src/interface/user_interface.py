import eel
import json

from manager.application_manager import ApplicationManager

application_manager: ApplicationManager


def init():
    global application_manager
    application_manager = ApplicationManager()
    eel.init('web')
    eel.start('html/index.html')


@eel.expose
def get_game_by_title(title=None):
    return json.dumps(application_manager.get_game_by_title(title).__dict__)


@eel.expose
def post_game_title(title):
    application_manager.post_game_title(title)
