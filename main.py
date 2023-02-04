def update_gamestate(gamestate, input):
    # code to update gamestate based on input
    # For example, if input is "move north", update the location in gamestate
    if input == "move north":
        gamestate["location"] = "North Room"
    # Add more logic here based on the game design
    ...
    return gamestate

def play_game():
    # Initialize game world
    gamestate = build_game_world()
    
    # Play the game
    while True:
        # Generate prompt
        prompt = generate_prompt(gamestate)
        
        # Get user input
        user_input = get_user_input(prompt)
        
        # Update gamestate based on user input
        gamestate = update_gamestate(gamestate, user_input)
        
        # Get response from OpenAI
        response = openai_response(prompt)
        
        # Update gamestate based on OpenAI response
        gamestate = update_gamestate(gamestate, response)

# Start the game
if __name__ == "__main__":
    play_game()
