import random
import toml
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

    def as_dict(self):
        return {
                "plot": self._plot,
                "characters": self._characters,
                "victim": self._victim,
                "locations": self._locations,
                "history": self._history,
        }

    def store(self):
        with open('.gamestate.toml', 'w') as f:
            toml.dump(self.as_dict(), f)

    def render_template(self) -> str:
        return template.render(**{
            "locations": self._locations,
            "characters": self._characters,
            "victim": self._victim,
            "history": self._history,
        })

    def add_history_entry(self, prompt: str, answer: str):
        self._history.append(f"USER: {prompt}\nGAME MASTER: {answer}")

    def solve_crime(self):
        self._crime_is_solved = True

    def is_game_finished(self):
        return self._crime_is_solved
