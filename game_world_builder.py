import random

from game_state import GameState
from global_config import config

random.seed(config["gameworld"]["seed"])


class GameWorldBuilder():
    def __init__(self):
        locations = [GameWorldBuilder.get_available_locations()[0]]
        characters = characters = GameWorldBuilder.get_available_characters()[0:4]
        plot = GameWorldBuilder.get_plot()

        # locations_n = random.choice([1, 1, 1, 2, 2, 3])
        # locations = random.sample(GameWorldBuilder.get_available_locations(), locations_n)
        # characters_n = random.randint(4, 6)
        # characters = characters = random.sample(GameWorldBuilder.get_available_characters(), characters_n)
        # plot = GameWorldBuilder.get_plot()

        self._gamestate: GameState = GameState(locations, characters, plot)

    @classmethod
    def get_available_characters(cls) -> list:
        return [
            {
                "name": "Sherlock Holmes",
                "description": "The legendary detective created by Sir Arthur Conan Doyle, known for his exceptional intellect, powers of observation, and deductive reasoning.",
            }, {
                "name": "Jean-Luc Picard",
                "description": "A fictional character and the captain of the USS Enterprise in the Star Trek: The Next Generation television series. He is a cultured, intelligent, and compassionate leader who values diplomacy over violence.",
            }, {
                "name": "Taylor Swift",
                "description": "A real-life American singer-songwriter known for her pop, country, and pop-rock music, as well as her personal life which is often the subject of media attention.",
            }, {
                "name": "Nancy Pearl",
                "description": "Librarian",
            }, {
                "name": "Austin Powers",
                "description": "A fictional character and the protagonist of the Austin Powers film series. He is a flamboyant, eccentric, and often clueless spy who parodies the spy genre.",
            }, {
                "name": "James Bond",
                "description": "The suave and debonair spy created by Ian Fleming, who uses his wit, charm, and deadly skills to protect his country and solve crimes.",
            }, {
                "name": "Gordon Ramsay",
                "description": "A real-life British chef, restaurateur, and television personality, best known for his fiery personality and critical commentary on cooking shows such as Hell's Kitchen and Kitchen Nightmares.",
            },
        ]

    @classmethod
    def get_available_locations(cls) -> list:
        return [
            {
                "name": "Library",
                "description": "A typical library as known like in the 1980s. Three levels, including a basement. Kind of comfy, with a corner with a couch and a few armchairs.",
            }, {
                "name": "Orient Express",
                "description": "The famous train from Agatha Christie's novel 'Murder on the Orient Express'.",
            }, {
                "name": "Elbphilharmony",
                "description": "The Elbphilharmonie is a concert hall located on the harbor of Hamburg and is known for its unique architecture and acoustics.",
            }, {
                "name": "USS Enterprise",
                "description": "The USS Enterprise (NCC-1701) is a starship of the United Federation of Planets in the Star Trek franchise.",
            }, {
                "name": "Old Elbe Tunnel",
                "description": "A pedestrian and vehicle tunnel in Hamburg, opened in 1911.",
            }, {
                "name": "Ohlsdorf Cemetery",
                "description": "The biggest rural cemetery in the world. Most of the people buried at the cemetery are civilians, but there is also a large number of victims of war from various nations.",
            }, {
                "name": "St. Michael's Church",
                "description": "St. Michael's Church is one of Hamburg's five Lutheran main churches and one of the most famous churches in the city. St. Michaelis is a landmark of the city and it is considered to be one of the finest Hanseatic Protestant baroque churches.",
            },
        ]

    @classmethod
    def get_plot(cls) -> str:
        return """
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
