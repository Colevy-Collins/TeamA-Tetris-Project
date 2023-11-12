from src.PygameDelegate import PygameDelegate
pygame = PygameDelegate()
from src.RandomDelegate import RandomDelegate
random = RandomDelegate()

NUM_OF_SHAPE_GRID_ROWS = 4
NUM_OF_SHAPE_GRID_COLUMNS = 4
ACCOUNT_FOR_NEXT_ROW = 4

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# codesmell - params should be assinged to a var and var used instead of param
# codesmell - long class
class BoardManager:
    def __init__(self, tetris_block, tetris_board, sound_manager, high_score_handler):
        self.tetris_block = tetris_block
        self.tetris_board = tetris_board     
        self.window_size = (400, 500)
        self.game_state = "start"  # or "gameover"
        self.figures = tetris_block
        self.sound_manager = sound_manager
        self.high_score_handler = high_score_handler
        self.score = 0
        self.high_score = self.high_score_handler.read_data()

    def create_figure(self, starting_shift_x, starting_shift_y):
        self.tetris_block.create_figure(starting_shift_x, starting_shift_y)
        if self.check_intersection():
            self.set_game_state("gameover")

    def check_intersection(self):
        is_intersection = False
        game_field = self.tetris_board.get_game_field()
        shift_in_x = self.tetris_block.get_shift_in_x()
        shift_in_y = self.tetris_block.get_shift_in_y()
        grid_block_height = self.tetris_board.get_grid_block_height()
        grid_block_width = self.tetris_board.get_grid_block_width()
        shape = self.get_shape()

        for current_row in range (NUM_OF_SHAPE_GRID_ROWS) :
            for current_column in range (NUM_OF_SHAPE_GRID_COLUMNS) :
                if current_row * ACCOUNT_FOR_NEXT_ROW  + current_column in shape:
                    is_emplty = 0
                    if current_row + shift_in_y > grid_block_height - 1 or \
                    current_column + shift_in_x > grid_block_width - 1 or \
                    current_column + shift_in_x < is_emplty or \
                    game_field[current_row + shift_in_y][ current_column  + shift_in_x] > is_emplty:
                        is_intersection = True
        return is_intersection
   
    """When a shape is purple, it seems to get deleted"""
    # maybe make a board_managment class with freeze, clear, check if filled, delete and all moves (maybe draw_figure)
    def freeze_figure(self):
        game_field = self.tetris_board.get_game_field()
        shape = self.tetris_block.get_shape()
        shift_in_x = self.tetris_block.get_shift_in_x()
        shift_in_y = self.tetris_block.get_shift_in_y()
        shape_color = self.tetris_block.get_current_figure_color()

        for current_row in range (NUM_OF_SHAPE_GRID_ROWS) :
            for current_column in range (NUM_OF_SHAPE_GRID_COLUMNS) :
                if current_row * ACCOUNT_FOR_NEXT_ROW  + current_column in shape:
                    game_field[ current_row + shift_in_y][ current_column  + shift_in_x] = shape_color

    def game_rules(self):
        starting_shift_x = 3
        starting_shift_y = 0  
        self.freeze_figure()
        self.create_figure(starting_shift_x, starting_shift_y)
    
    def move_to_bottom(self):
        while not self.check_intersection():
            self.tetris_block.set_shift_in_y(self.tetris_block.get_shift_in_y() + 1)
        self.tetris_block.set_shift_in_y(self.tetris_block.get_shift_in_y() - 1)
        self.game_rules()

        self.sound_manager.play_space_sound()

    def move_down(self):
        self.tetris_block.set_shift_in_y(self.tetris_block.get_shift_in_y() + 1)
        if self.check_intersection():
            self.tetris_block.set_shift_in_y(self.tetris_block.get_shift_in_y() - 1)
            self.sound_manager.play_landing_sound()
            self.game_rules()

    def move_sideways(self, player_change_in_x):
        shift_in_x = self.tetris_block.get_shift_in_x()

        self.tetris_block.set_shift_in_x(shift_in_x + player_change_in_x)
        if self.check_intersection():
            self.tetris_block.set_shift_in_x(shift_in_x)

        self.sound_manager.play_move_sound()

    def rotate_figure(self):      
        current_rotation = self.tetris_block.get_current_rotation()
        figures = self.tetris_block.get_figure() # add geter to tetris block for this.
        current_figure_type = self.tetris_block.get_current_figure_type()
        
        self.tetris_block.set_current_rotation((self.tetris_block.get_current_rotation() + 1) % len(figures[current_figure_type]))
        if self.check_intersection():
            self.tetris_block.set_current_rotation((self.tetris_block.get_current_rotation() - 1)  % len(figures[current_figure_type]))
        
        self.sound_manager.play_move_sound()

    def draw_figure(self, screen):
        shape = self.get_shape()
        color = self.tetris_block.get_colors()[self.tetris_block.get_current_figure_color()] # get from board
        start_x_position = self.tetris_board.get_start_x_position()
        start_y_position = self.tetris_board.get_start_y_position()
        size_of_grid_block = self.tetris_board.get_size_of_grid_block()
        shift_in_x = self.tetris_block.get_shift_in_x()
        shift_in_y = self.tetris_block.get_shift_in_y()

        for current_row in range (NUM_OF_SHAPE_GRID_ROWS) :
            for current_column in range (NUM_OF_SHAPE_GRID_COLUMNS) :
                position = current_row * ACCOUNT_FOR_NEXT_ROW  +  current_column 
                if position in shape:
                    pygame.draw.rect(screen, color,
                                    [start_x_position  + size_of_grid_block * ( current_column  + shift_in_x) + 1,
                                    start_y_position + size_of_grid_block * ( current_row + shift_in_y) + 1,
                                    size_of_grid_block - 2, size_of_grid_block - 2])
 

    def get_shape(self):
        return self.tetris_block.get_shape()
    
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
