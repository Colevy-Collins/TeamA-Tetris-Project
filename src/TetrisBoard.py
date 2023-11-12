from src.PygameDelegate import PygameDelegate
pygame = PygameDelegate()

from src.RandomDelegate import RandomDelegate
random = RandomDelegate()

from src.Button import Button

NUM_OF_SHAPE_GRID_ROWS = 4
NUM_OF_SHAPE_GRID_COLUMNS = 4
ACCOUNT_FOR_NEXT_ROW = 4

COLORS = (
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# codesmell - params should be assinged to a var and var used instead of param
# codesmell - long class
class TetrisBoard:
    def __init__(self):
        self.size_of_grid_block = 20
        self.start_x_position = 100
        self.start_y_position = 60
        self.grid_block_height = 0
        self.grid_block_width = 0        
        self.window_size = (400, 500)
        self.game_field = []
        self.colors = (
            (0, 0, 0), # can not use index 0
            (120, 37, 179),
            (100, 179, 179),
            (80, 34, 22),
            (80, 134, 22),
            (180, 34, 22),
            (180, 34, 122),
        )
        self.board_color = WHITE


    # make a class that connects pygame to this one and remove pygame form class
    def draw_game_board(self, screen):
        screen.fill(self.board_color)
        game_field = self.get_game_field()
        grid_block_height = self.get_grid_block_height()
        grid_block_width = self.get_grid_block_width()
        start_x_position = self.get_start_x_position()
        start_y_position = self.get_start_y_position()	
        size_of_grid_block = self.get_size_of_grid_block()

        for current_row in range(grid_block_height):
            for current_column in range(grid_block_width):
                pygame.draw.rect(screen, GRAY, [start_x_position + size_of_grid_block *  current_column , start_y_position + size_of_grid_block * current_row, size_of_grid_block, size_of_grid_block], 1)
                if game_field[ current_row ][ current_column ] > 0:
                    pygame.draw.rect(screen, self.colors[game_field[ current_row ][ current_column ]],
                                    [start_x_position + size_of_grid_block * current_column + 1, start_y_position + size_of_grid_block * current_row + 1, size_of_grid_block - 2, size_of_grid_block - 1])

    def initialize_board(self, height, width):

        self.set_grid_block_height(height)
        self.set_grid_block_width(width)
        self.set_game_field([])
        grid_block_height = self.get_grid_block_height()
        grid_block_width = self.get_grid_block_width()
        is_empty = 0
        for current_row in range(grid_block_height):
            new_line = [ is_empty ] * grid_block_width # polymorphism using * 
            self.append_to_game_field(new_line)


    # Getter and setter for size_of_grid_block
    def get_size_of_grid_block(self):
        return self.size_of_grid_block

    def set_size_of_grid_block(self, value):
        self.size_of_grid_block = value

    # Getter and setter for start_x_position
    def get_start_x_position(self):
        return self.start_x_position

    def set_start_x_position(self, value):
        self.start_x_position = value

    # Getter and setter for start_y_position
    def get_start_y_position(self):
        return self.start_y_position

    def set_start_y_position(self, value):
        self.start_y_position = value

    # Getter and setter for grid_block_height
    def get_grid_block_height(self):
        return self.grid_block_height

    def set_grid_block_height(self, value):
        self.grid_block_height = value

    # Getter and setter for grid_block_width
    def get_grid_block_width(self):
        return self.grid_block_width

    def set_grid_block_width(self, value):
        self.grid_block_width = value

        # Getter and setter for window_size
    def get_window_size(self):
        return self.window_size

    def set_window_size(self, value):
        self.window_size = value

    # Getter and setter for game_field
    def get_game_field(self):
        return self.game_field

    def set_game_field(self, value):
        self.game_field = value

    # Method to append to game_field
    def append_to_game_field(self, value):
        self.game_field.append(value)

        # Getter and setter for colors
    def get_colors(self):
        return self.colors

    def set_colors(self, value):
        self.colors = value

    def set_board_color(self, value):
        self.board_color = value
    def get_board_color(self):
        return self.board_color
    # Method to append to colors
    def append_to_colors(self, value):
        self.colors.append(value)
