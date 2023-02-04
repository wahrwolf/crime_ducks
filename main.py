def update_gamestate(gamestate, input):
    response = openai_client.send_prompt(input)
    # code to update gamestate based on response
    # For example, if response is "You are now in the North Room", update the location in gamestate
    if "You are now in the North Room" in response:
        gamestate["location"] = "North Room"
    # Add more logic here based on the game design and OpenAI response
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
