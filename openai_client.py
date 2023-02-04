import openai
import toml

config = toml.load("config.toml")
openai.api_key = config["openai"]["api_key"]

# OpenAI client
def get_response(prompt):
    response = openai.Completion.create(
        engine=config["openai"]["model"],
        prompt=prompt,
        max_tokens=config["openai"].get("max_tokens", 2048),
        n=1,
        stop=None,
        temperature=config["openai"].get("temperature", 0.7)
    ).choices[0].text
    return response
