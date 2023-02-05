import signal
import sys
from logging import warning
from game_server import GameServer
from game_client import GameClient


def sigint_handler(signal, frame):
    warning("You gave up. Bye!")
    sys.exit(0)

if __name__ == "__main__":
    server = GameServer()
    client = GameClient()
    server.attach_player(client)

    signal.signal(signal.SIGINT, sigint_handler)

    try:
        server.play_game()
    except Exception:
        pass
