import random
import toml
from jinja2 import Environment, FileSystemLoader

config = toml.load("config.toml")

random.seed(config["gameworld"]["seed"])

env = Environment(loader=FileSystemLoader(''))
template = env.get_template(config["gameworld"]["template_path"])


class GameState():
    def __init__(self, locations: list, characters: list, plot: str):
        self._characters = characters
        self._locations = locations
        self._plot = plot
        self._victim = random.choice(characters)
        self._history = []

    def render_template(self) -> str:
        print(self._locations)
        return template.render(**{
            "locations": self._locations,
            "characters": self._characters,
            "victim": self._victim,
            "history": self._history,
        })

    def add_history_entry(self, value: str):
        self._history.append(value)


class GameWorldBuilder():
    def __init__(self):
        self._gamestate: GameState = GameState(
            [GameWorldBuilder.get_available_locations()[0]],
            GameWorldBuilder.get_available_characters()[0:4],
            GameWorldBuilder.get_available_characters()[2],
        )

    @classmethod
    def get_available_characters(cls) -> list:
        return [
            {
                "name": "Sherlock Holmes",
                "description": "a character from the Sherlock Holmes franchise.",
            }, {
                "name": "Jean-Luc Picard",
                "description": "a character from the Star Trek franchise.",
            }, {
                "name": "Taylor Swift",
                "description": "the pop star",
            }, {
                "name": "Nancy Pearl",
                "description": "Librarian",
            }, {
                "name": "Austin Powers",
                "description": "a character from the Austin Powers franchise.",
            }, {
                "name": "James Bond",
                "description": "a character from the James Bond franchise.",
            }, {
                "name": "Beckett Mariner",
                "description": "a character from the star trek franchise. Ensign in the Starfleet",
            }, {
                "name": "Gordon Ramsay",
                "description": "A famous cook from TV.",
            },
        ]

    @classmethod
    def get_available_locations(cls) -> list:
        return [
            {
                "name": "Library",
                "description": "A typical library as known like in the 1980s. Three levels, including a basement. Kind of comfy, with a corner with a couch and a few armchairs.",
            },
        ]

    @classmethod
    def get_plot(cls) -> str:
        return """
        Sure, here's a plot for the text-based RPG in the Library:

        It's a typical day in the library, with each character carrying out their own business. Sherlock Holmes is investigating a case, Jean-Luc Picard is reading a book, Taylor Swift is writing music, and Nancy Pearl is busy with library work.

        Suddenly, Taylor Swift is found dead in one of the aisles of the library. The players must find out who the killer is and what their motives were.

        After investigating the scene, it becomes clear that the killer must have been one of the four characters in the library at the time of the murder. The player must use their detective skills to gather clues and interrogate the suspects to find out who committed the crime.
 
        The killer turns out to be Nancy Pearl, the librarian. She had a personal grudge against Taylor Swift, who had been causing trouble in the library and being disrespectful to Nancy. Nancy snapped and killed Taylor in a fit of rage.

        It's up to the player to gather the evidence and put the pieces together to figure out who the killer is and bring them to justice.
        """

    def get_gamestate(self):
        return self._gamestate


def build_game_world():
    gameworld_builder = GameWorldBuilder()
    return gameworld_builder.get_gamestate()


# if __name__ == "__main__":
#     state = build_game_world()
#     print(state.render_template())
