![](assets/detective_duck.png)

# Goal
Welcome to the game! You are Robert McDuck, a crime solving duck.
You will have to investigate the crime scene and interrogate the four suspects.
You must use your wit and charm to uncover the truth and find the killer. Good luck!

# Installation
- Install pipenv (from your local package manager) or by `pip install --user pipenv`
- Install all packages with pipenv `pipenv install`
- Get your openai_api token (https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)
- Put you key in `.openai_key`
- Start the game by `pipenv run python main.py`

# Commands
You can use meta commands to control the game.
- `!restart`: Generate a new scenario and start from the beginning
- `!end`: End the current game, and reveal the plot.
- `!show plot`: Show the current game plot without ending the game

# *BROKEN* Telegram Bot
- Get you telegram_api token (https://core.telegram.org/bots#how-do-i-create-a-bot)
- Put you key in `.telegram_api_token`
- Start the game by `pipenv run python telegram_bot.py`

Currently the bot is broken, because some loop is not coded properly.
Tbh we hacked the project in a weekend lost any roadmap or further docs.
If you fix it, please send a PR

# Other Infos
checkout https://owasp.org/www-project-top-10-for-large-language-model-applications/ for speedruns
