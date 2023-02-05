from game_client import GameClient
from game_world_builder import build_game_world
from prompt_generator import generate_prompt, generate_plot_user_info_prompt, generate_case_solved_query_prompt
from user_questioner import get_user_input
from openai_client import get_response

class GameServer:
    def __init__(self):
        self.played_turns = 0

    def start_game(self):
        self.played_turns = 0

        self.gamestate = build_game_world()
        plot_info_prompt = generate_plot_user_info_prompt(self.gamestate)
        plot_info_response = get_response(plot_info_prompt)
        self.player.print_message(plot_info_response)

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


    def play_turn(self):
        self.last_player_response = self.player.read_line()
        self.tell_ai_about_player_decision()
        self.update_gamestate()
        self.player.show_response(self.last_ai_response)
        self.played_turns += 1

    def check_if_game_is_finished(self):
        case_closed_prompt = generate_case_solved_query_prompt(self.gamestate)
        case_closed_response = get_response(case_closed_prompt).strip()
        if case_closed_response.strip().lower() == "yes":
            self.gamestate.solve_crime()

    def greet_player(self):
        self.player.print_message("Chatbot Crime Busters 🦆", show_underline=False)
        self.player.print_message("------------------------", show_underline=False)

    def thank_player(self):
        self.player.print_message((f"You busted the crime after {self.played_turns} Questions. You won!"))

    def play_game(self):
        self.start_game()

        while not self.gamestate.is_game_finished():
            self.play_turn()
            self.check_if_game_is_finished()
        self.thank_player()
