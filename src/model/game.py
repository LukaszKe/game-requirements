from model.components import Components


class Game:
    name: str
    is_free: bool
    short_description: str
    header_image: str  # url
    pc_requirements_minimum: Components
    pc_requirements_recommended: Components
    publishers: list
    price: str
    metacritic_score: int = ''
    categories: list
    release_date: str
