class TetrisGame:
    def __init__(self):
        self.window_size = (400, 500)
        self.game_state = "start"  # or "gameover"
        self.game_field = []

    # Getter and setter for window_size
    def get_window_size(self):
        return self.window_size

    def set_window_size(self, value):
        self.window_size = value

    # Getter and setter for game_state
    def get_game_state(self):
        return self.game_state

    def set_game_state(self, value):
        if value == "start" or value == "gameover":
            self.game_state = value
        else:
            self.game_state = "gameover"

    # Getter and setter for game_field
    def get_game_field(self):
        return self.game_field

    def set_game_field(self, value):
        self.game_field = value

    # Method to append to game_field
    def append_to_game_field(self, value):
        self.game_field.append(value)
