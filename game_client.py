class GameClient:
    def __init__(self):
        pass

    def print_message(self, message: str, show_underline=True):
        print(message)
        if show_underline:
            print("----")

    def read_line(self, prompt="Q> "):
        user_input = input(prompt)
        return user_input

    def show_response(self, response: str):
        self.print_message(f"A> {response}", show_underline=False)

