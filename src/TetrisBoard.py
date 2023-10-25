from src.PygameDelegate import PygameDelegate
pygame = PygameDelegate()

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

# codesmell - params should be assinged to a var and var used instead of param
# codesmell - long class
class TetrisBoard:
    def __init__(self):
        self.size_of_grid_block = 20
        self.start_x_position = 100
        self.start_y_position = 60
        self.grid_block_height = 0
        self.grid_block_width = 0

    def check_intersection(self, tetris_block, tetris_game):
        is_intersection = False
        game_field = tetris_game.get_game_field()
        for current_row in range (NUM_OF_SHAPE_GRID_ROWS) :
            for current_column in range (NUM_OF_SHAPE_GRID_COLUMNS) :
                if current_row * ACCOUNT_FOR_NEXT_ROW  + current_column in tetris_block.get_shape():
                    is_emplty = 0
                    if current_row + tetris_block.get_shift_in_y() > self.get_grid_block_height() - 1 or \
                    current_column + tetris_block.get_shift_in_x() > self.get_grid_block_width() - 1 or \
                    current_column + tetris_block.get_shift_in_x() < is_emplty or \
                    game_field[current_row + tetris_block.get_shift_in_y()][ current_column  + tetris_block.get_shift_in_x()] > is_emplty:
                        is_intersection = True
        return is_intersection
   
    """The freeze_figure method has a bug where it looks like it is not freezing a figure to the board.
        This bug does not appear to be consistent, with most figures being frozen as they should.
        This bug involves the create_figure method. This bug happens when you change create_figure from
        a global method to either an internal method or a called method. I have not been able to figure out why,
        but all other functions work. I think it may have to do with the refreshing of the game."""
    # maybe make a board_managment class with freeze, clear, check if filled, delete and all moves (maybe draw_figure)
    def freeze_figure(self, tetris_block, tetris_game):
        game_field = tetris_game.get_game_field()
        starting_shift_x = 3
        starting_shift_y = 0
        for current_row in range (NUM_OF_SHAPE_GRID_ROWS) :
            for current_column in range (NUM_OF_SHAPE_GRID_COLUMNS) :
                if current_row * ACCOUNT_FOR_NEXT_ROW  + current_column in tetris_block.get_shape():
                    game_field[ current_row + tetris_block.get_shift_in_y()][ current_column  + tetris_block.get_shift_in_x()] = tetris_block.get_current_figure_color()
        self.clear_lines(tetris_game)
        tetris_block.create_figure(starting_shift_x, starting_shift_y) 
        if self.check_intersection(tetris_block, tetris_game):
            tetris_game.set_game_state("gameover")

    def clear_lines(self, tetris_game):
        start_of_range = 1
        for current_row in range(start_of_range, self.get_grid_block_height()):
            if self.check_if_row_is_filled(current_row, tetris_game):
                self.delete_row(current_row, tetris_game)

    def check_if_row_is_filled(self, current_row, tetris_game):
        is_emplty = 0
        game_field = tetris_game.get_game_field()
        for current_column in range(self.get_grid_block_width()):
            if game_field[ current_row ][ current_column ] == 0:
                is_emplty += 1
        return is_emplty == 0
            
    def delete_row(self, current_row, tetris_game):
        end_of_range = 1
        size_of_step_through_range = -1
        game_field = tetris_game.get_game_field()
        for current_row_above in range(current_row, end_of_range, size_of_step_through_range):
            for current_column in range(self.get_grid_block_width()):
                game_field[current_row_above][ current_column ] = game_field[current_row_above - 1][ current_column ]
    # maybe make moves sub classes of a moves class and use poly
    def move_to_bottom(self, tetris_block, tetris_game):
        
        while not self.check_intersection(tetris_block, tetris_game):
            tetris_block.set_shift_in_y(tetris_block.get_shift_in_y() + 1)
        tetris_block.set_shift_in_y(tetris_block.get_shift_in_y() - 1)
        self.freeze_figure(tetris_block, tetris_game)

    def move_down(self, tetris_block, tetris_game):
        
        tetris_block.set_shift_in_y(tetris_block.get_shift_in_y() + 1)
        if self.check_intersection(tetris_block, tetris_game):
            tetris_block.set_shift_in_y(tetris_block.get_shift_in_y() - 1)
            self.freeze_figure(tetris_block, tetris_game)

    def move_sideways(self, player_change_in_x, tetris_block, tetris_game):
        old_x = tetris_block.get_shift_in_x()
        tetris_block.set_shift_in_x(tetris_block.get_shift_in_x() + player_change_in_x)
        if self.check_intersection(tetris_block, tetris_game):
            tetris_block.set_shift_in_x(old_x)

    def rotate_figure(self, tetris_block, tetris_game):      
        old_rotation = tetris_block.get_current_rotation()
        tetris_block.set_current_rotation((tetris_block.get_current_rotation() + 1) % len(tetris_block.Figures[tetris_block.get_current_figure_type()])) #codesmell
        if self.check_intersection(tetris_block, tetris_game):
            tetris_block.set_current_rotation(old_rotation)

    def draw_figure(self, screen, tetris_block):
        for current_row in range (NUM_OF_SHAPE_GRID_ROWS) :
            for current_column in range (NUM_OF_SHAPE_GRID_COLUMNS) :
                p = current_row * ACCOUNT_FOR_NEXT_ROW  +  current_column 
                if p in tetris_block.get_shape():
                    pygame.draw.rect(screen, COLORS[tetris_block.get_current_figure_color()],
                                    [self.get_start_x_position()  + self.get_size_of_grid_block() * ( current_column  + tetris_block.shift_in_x) + 1,
                                    self.get_start_y_position() + self.get_size_of_grid_block() * ( current_row + tetris_block.shift_in_y) + 1,
                                    self.get_size_of_grid_block() - 2, self.get_size_of_grid_block() - 2])

    # make a class that connects pygame to this one and remove pygame form class
    def draw_game_board(self, screen, tetris_game):
        screen.fill(WHITE)
        game_field = tetris_game.get_game_field()

        for current_row in range(self.get_grid_block_height()):
            for current_column in range(self.get_grid_block_width()):
                pygame.draw.rect(screen, GRAY, [self.get_start_x_position() + self.get_size_of_grid_block() *  current_column , self.get_start_y_position() + self.get_size_of_grid_block() * current_row, self.get_size_of_grid_block(), self.get_size_of_grid_block()], 1)
                if game_field[ current_row ][ current_column ] > 0:
                    pygame.draw.rect(screen, COLORS[game_field[ current_row ][ current_column ]],
                                    [self.get_start_x_position() + self.get_size_of_grid_block() * current_column + 1, self.get_start_y_position() + self.get_size_of_grid_block() * current_row + 1, self.get_size_of_grid_block() - 2, self.get_size_of_grid_block() - 1])

    def initialize_board(self, height, width, tetris_game):

        self.set_grid_block_height(height)
        self.set_grid_block_width(width)
        tetris_game.set_game_field([])
        tetris_game.set_game_state("start")
        is_empty = 0
        for current_row in range(self.get_grid_block_height()):
            new_line = [ is_empty ] * self.get_grid_block_width() # polymorphism using * 
            tetris_game.append_to_game_field(new_line)


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
