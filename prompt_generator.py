# Prompt generator

TEMPLATE = """
You are the game master of a text-based role playing game.
Below, you will receive a user input, which you will answer as the game master would.

The plot of the game is this:
{plot}

The characters are:
{characters}

THE CONVERSATION SO FAR:
{history}

USER PROMPT: {user_prompt}

GAME MASTER RESPONSE:
"""

def generate_prompt(gamestate, user_prompt):
    # code to generate prompt based on gamestate
    plot = gamestate._plot
    characters = "\n".join(f"{c['name']}: {c['description']}" for c in gamestate._characters)
    history = "\n".join(gamestate._history)
    prompt = TEMPLATE.format(plot=plot, characters=characters, user_prompt=user_prompt, history=history)
    return prompt
