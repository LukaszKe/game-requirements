from model.game_requirements import GameRequirements


class Game:
    name: str
    is_free: bool
    short_description: str
    header_image: str  # url
    pc_requirements_minimum: GameRequirements
    pc_requirements_recommended: GameRequirements
    publishers: list
    price: str
    metacritic_score: int
    categories: list
    release_date: str
