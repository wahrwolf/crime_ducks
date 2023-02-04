from game_world_builder import build_game_world
from prompt_generator import generate_prompt
from user_questioner import get_user_input
from openai_client import get_response

def update_gamestate(gamestate, response):
    gamestate.add_history_entry(response)
    return gamestate


def play_game():
    # Initialize game world
    gamestate = build_game_world()
    
    # Play the game
    while True:
        # Get user input
        user_prompt = get_user_input(gamestate)

        prompt = generate_prompt(gamestate, user_prompt)
        
        # Get response from OpenAI
        response = get_response(prompt)

        print(f"A> {response}")
        
        # Update gamestate based on OpenAI response
        gamestate = update_gamestate(gamestate, response)


if __name__ == "__main__":
    print("Chatbot Crime Busters 🦆")
    play_game()
