from global_config import config, jinja_env
# Prompt generator

def generate_prompt(gamestate, user_prompt):
    # code to generate prompt based on gamestate
    template = jinja_env.get_template(config["prompts"]["user_template_path"])
    prompt = template.render(dict(user_prompt=user_prompt, **gamestate.as_dict()))
    return prompt

def generate_plot_user_info_prompt(gamestate):
    template = jinja_env.get_template(config["prompts"]["plot_template_path"])
    prompt = template.render(gamestate.as_dict())
    return prompt

def generate_case_solved_query_prompt(gamestate):
    template = jinja_env.get_template(config["prompts"]["case_closed_template_path"])
    prompt = template.render(gamestate.as_dict())
    return prompt
