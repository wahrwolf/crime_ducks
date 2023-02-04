import random

from global_config import config, jinja_env

template = jinja_env.get_template(config["gameworld"]["template_path"])


class GameState():
    def __init__(self, locations: list, characters: list, plot: str):
        self._characters = characters
        self._locations = locations
        self._plot = plot
        self._victim = random.choice(characters)
        self._history = []
        self._crime_is_solved = False

    def render_template(self) -> str:
        return template.render(**{
            "locations": self._locations,
            "characters": self._characters,
            "victim": self._victim,
            "history": self._history,
        })

    def add_history_entry(self, value: str):
        self._history.append(value)

    def solve_crime(self):
        this._crime_is_solved = True

    def is_game_finished(self):
        return self.is_game_finished
