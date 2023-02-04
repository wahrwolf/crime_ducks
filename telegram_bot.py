from game_world_builder import build_game_world
from prompt_generator import generate_prompt
from prompt_generator import generate_plot_user_info_prompt
from openai_client import get_response

import telebot
import toml

config = toml.load("config.toml")
with open(config["telegram"]["secret_file"]) as f:
    API_TOKEN = f.read().splitlines()[0]

bot = telebot.TeleBot(API_TOKEN)

def update_gamestate(gamestate, user_prompt, response):
    gamestate.add_history_entry(user_prompt, response)
    return gamestate

def play_game(chat_id):
    # Initialize game world
    gamestate = build_game_world()
    
    plot_info_prompt = generate_plot_user_info_prompt(gamestate)

    plot_info_response = get_response(plot_info_prompt)

    bot.send_message(chat_id, plot_info_response)

    # Play the game
    while not gamestate.is_game_finished():
        # Get user input
        user_prompt = bot.send_message(chat_id, "What would you like to do?").text

        prompt = generate_prompt(gamestate, user_prompt)
        
        # Get response from OpenAI
        response = get_response(prompt)

        bot.send_message(chat_id, f"A> {response}")
        
        # Update gamestate based on OpenAI response
        gamestate = update_gamestate(gamestate, user_prompt, response)

    bot.send_message(chat_id, "You busted the crime. You won!")

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Welcome to the Chatbot Crime Busters 🦆")
    play_game(message.chat.id)

if __name__ == "__main__":
    bot.polling()
