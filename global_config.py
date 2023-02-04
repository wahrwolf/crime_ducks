import toml
from jinja2 import Environment, FileSystemLoader

config = toml.load("config.toml")
jinja_env = Environment(loader=FileSystemLoader(''))
