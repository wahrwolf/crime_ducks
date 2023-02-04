from game_world_builder import build_game_world
from prompt_generator import generate_prompt
from prompt_generator import generate_plot_user_info_prompt
from user_questioner import get_user_input
from openai_client import get_response

def update_gamestate(gamestate, user_prompt, response):
    gamestate.add_history_entry(user_prompt, response)
    return gamestate


def play_game():
    # Initialize game world
    gamestate = build_game_world()
    
    plot_info_prompt = generate_plot_user_info_prompt(gamestate)

    plot_info_response = get_response(plot_info_prompt)

    print(plot_info_response)
    print("----")

    # Play the game
    while not gamestate.is_game_finished():
        # Get user input
        user_prompt = get_user_input(gamestate)

        prompt = generate_prompt(gamestate, user_prompt)
        
        # Get response from OpenAI
        response = get_response(prompt)

        print(f"A> {response}")
        
        # Update gamestate based on OpenAI response
        gamestate = update_gamestate(gamestate, user_prompt, response)

    print("You busted the crime. You won!")


if __name__ == "__main__":
    print("Chatbot Crime Busters 🦆")
    print("------------------------")

    play_game()
