NUM_OF_SHAPE_GRID_ROWS = 4
NUM_OF_SHAPE_GRID_COLUMNS = 4
ACCOUNT_FOR_NEXT_ROW = 4

class GameRules:
    def __init__(self, tetris_block, tetris_board):
        self.tetris_board = tetris_board
        self.tetris_block =  tetris_block

    def check_intersection(self):
        is_intersection = False
        game_field = self.tetris_board.get_game_field()
        shift_in_x = self.tetris_block.get_shift_in_x()
        shift_in_y = self.tetris_block.get_shift_in_y()
        grid_block_height = self.tetris_board.get_grid_block_height()
        grid_block_width = self.tetris_board.get_grid_block_width()
        shape = self.tetris_block.get_shape()

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
    
    def game_rules(self):
        starting_shift_x = 3
        starting_shift_y = 0  
        self.freeze_figure()
        self.create_figure(starting_shift_x, starting_shift_y)

    def create_figure(self, starting_shift_x, starting_shift_y):
        self.tetris_block.create_figure(starting_shift_x, starting_shift_y)
        if self.check_intersection():
            self.set_game_state("gameover")
   
    """The freeze_figure method has a bug where it looks like it is not freezing a figure to the board.
        This bug does not appear to be consistent, with most figures being frozen as they should.
        This bug involves the create_figure method. This bug happens when you change create_figure from
        a global method to either an internal method or a called method. I have not been able to figure out why,
        but all other functions work. I think it may have to do with the refreshing of the game."""
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
