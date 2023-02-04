class GameWorldBuilder:
    def __init__(self):
        self.gamestate = {}

    def build_characters(self, character_builder):
        self.gamestate["characters"] = character_builder.build()
        return self

    def build_plot(self, plot_builder):
        self.gamestate["plot"] = plot_builder.build()
        return self

    def build_scenes(self, scene_builder):
        self.gamestate["scenes"] = scene_builder.build()
        return self

class CharacterBuilder:
    def build(self):
        # code to build characters
        characters = ...
        return characters

class PlotBuilder:
    def build(self):
        # code to build plot
        plot = ...
        return plot

class SceneBuilder:
    def build(self):
        # code to build scenes
        scenes = ...
        return scenes

def build_game_world():
    gameworld_builder = GameWorldBuilder()
    gameworld_builder.build_characters(CharacterBuilder()) \
                     .build_plot(PlotBuilder()) \
                     .build_scenes(SceneBuilder())
    return gameworld_builder.gamestate
