from game_client import GameClient
from game_world_builder import build_game_world
from prompt_generator import generate_prompt, generate_plot_user_info_prompt, generate_case_solved_query_prompt
from user_questioner import get_user_input
from openai_client import get_response, will_be_flagged_by_moderation

class GameServer:

    commands = {}

    def __init__(self, disable_moderation=False, enable_commands=True):
        self.played_turns = 0
        self.moderation_disabled = disable_moderation
        self.commands_enabled = enable_commands

        self.commands["restart"] = self.start_game
        self.commands["end"] = self.end_game
        self.commands["show plot"] = self.show_plot

    def end_game(self):
        self.gamestate.solve_crime()

    def start_game(self):
        self.played_turns = 0

        self.gamestate = build_game_world()
        plot_info_prompt = generate_plot_user_info_prompt(self.gamestate)
        plot_info_response = get_response(plot_info_prompt)
        self.player.print_message(plot_info_response)

    def show_plot(self):
        self.player.print_message(self.gamestate.as_dict()["plot"])

    def attach_player(self, player: GameClient):
        self.player = player

    def update_gamestate(self):
        self.gamestate.add_history_entry(
                self.last_player_response,
                self.last_ai_response
        )
        self.gamestate.store()

    def tell_ai_about_player_decision(self):
        prompt = generate_prompt(self.gamestate, self.last_player_response)
        self.last_ai_response = get_response(prompt)

    def handle_command(self, command:str):
        if command in self.commands:
            try:
                response = self.commands[command]()
            except Exception as error:
                self.player.print_message(f"!!!Command failed due to: {error}!!!")
            else:
                if response:
                    self.player.print_message(response)
        else:
                self.player.print_message("!!!Command unknown!!!")
        


    def play_turn(self):
        player_action = self.player.read_line()
        while self.commands_enabled and player_action.startswith("!"):
            self.handle_command(player_action[1::])
            if self.gamestate.is_game_finished():
                return
            player_action = self.player.read_line()

        while not self.moderation_disabled and will_be_flagged_by_moderation(player_action):
            self.player.print_message("!!! Your response does not comply with the moderation guideline !!!")
            player_action = self.player.read_line()
        self.last_player_response = player_action

        self.tell_ai_about_player_decision()
        self.update_gamestate()
        self.player.show_response(self.last_ai_response)
        self.played_turns += 1

    def check_if_game_is_finished(self):
        if self.gamestate.is_game_finished():
            return
        case_closed_prompt = generate_case_solved_query_prompt(self.gamestate)
        case_closed_response = get_response(case_closed_prompt).strip()
        if case_closed_response.strip().lower() == "yes":
            self.end_game()

    def greet_player(self):
        self.player.print_message("Chatbot Crime Busters 🦆", show_underline=False)
        self.player.print_message("------------------------", show_underline=False)

    def thank_player(self):
        self.player.print_message(f"You busted the crime after {self.played_turns} Questions. You won!")
        self.player.print_message("\n\nThe plot was:")
        self.show_plot()

    def play_game(self):
        self.start_game()

        while not self.gamestate.is_game_finished():
            self.play_turn()
            self.check_if_game_is_finished()
        self.thank_player()
