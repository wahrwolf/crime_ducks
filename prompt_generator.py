# Prompt generator

TEMPLATE = """
You are the game master of a text-based role playing game.
Below, you will receive a user input, which you will answer as the game master would.

The game is about solving a crime by deducing the murderer based on the responses of the involved characters to the user's questions.

The game will be played in the following locations:

The plot of the game is this:
{plot}

The available locations are this:
{locations}

There is one player.
The characters (aside form the player) are:
{characters}

Murder victim: {{ victim }}

Murderer: not the victim and not the player and not the game master. You have to choose the killer.

HERE IS THE CONVERSATION UNTIL NOW:
{history}

USER: {user_prompt}
GAME MASTER RESPONSE: 
"""

def generate_prompt(gamestate, user_prompt):
    # code to generate prompt based on gamestate
    plot = gamestate._plot
    characters = "\n".join(f"{c['name']}: {c['description']}" for c in gamestate._characters)
    history = "\n".join(gamestate._history)
    locations = "\n".join(f"{c['name']}: {c['description']}" for c in gamestate._locations)
    prompt = TEMPLATE.format(plot=plot, characters=characters, user_prompt=user_prompt, history=history, victime=gamestate._victim, locations=locations)

    # print(prompt)

    return prompt
