import random

from game_state import GameState
from global_config import config, jinja_env
from openai_client import get_response

if config["gameworld"].get("seed", None):
    print("set the seed: {}".format(config["gameworld"]["seed"]))
    random.seed(config["gameworld"]["seed"])


class GameWorldBuilder():
    def __init__(self):
        # locations = [GameWorldBuilder.get_available_locations()[0]]
        # characters = characters = GameWorldBuilder.get_available_characters()[0:4]
        # plot = GameWorldBuilder.get_plot()

        locations_n = random.choice([1, 1, 1, 2, 2, 3])
        locations = random.sample(GameWorldBuilder.get_available_locations(), locations_n)
        characters_n = random.randint(4, 6)
        characters = characters = random.sample(GameWorldBuilder.get_available_characters(), characters_n)
        victim = random.choice(characters)
        characters.remove(victim)
        plot = GameWorldBuilder.get_plot({"locations": locations, "characters": characters, "victim": victim})

        self._gamestate: GameState = GameState(locations, characters, victim, plot)

    @classmethod
    def get_available_characters(cls) -> list:
        return config["gameworld"]["characters"]

    @classmethod
    def get_available_locations(cls) -> list:
        return config["gameworld"]["locations"]

    @classmethod
    def get_plot(cls, opts) -> str:
        # return config["gameworld"]["plot"]
        template = jinja_env.get_template(config["gameworld"]["template_path"])
        prompt = template.render(**opts)
        response = get_response(prompt)
        return prompt

    def get_gamestate(self):
        return self._gamestate


def build_game_world():
    gameworld_builder = GameWorldBuilder()
    return gameworld_builder.get_gamestate()


# if __name__ == "__main__":
#     state = build_game_world()
#     print(state.render_template())
