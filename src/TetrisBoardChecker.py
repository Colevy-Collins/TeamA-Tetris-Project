class BoardChecker:
    def __init__(self, tetris_board ):
        self.tetris_board = tetris_board

    def clear_lines(self):
        grid_block_height = self.tetris_board.get_grid_block_height()
        start_of_range = 1
    
        for current_row in range(start_of_range, grid_block_height):
            if self.check_if_row_is_filled(current_row):
                self.delete_row(current_row)

    def check_if_row_is_filled(self, current_row):
        grid_block_width = self.tetris_board.get_grid_block_width()
        game_field = self.tetris_board.get_game_field()
        is_empty = 0
        for current_column in range(grid_block_width):
            if game_field[ current_row ][ current_column ] == is_empty:
                is_empty += 1
        return is_empty == 0
            
    def delete_row(self, current_row):
        game_field = self.tetris_board.get_game_field()
        grid_block_width = self.tetris_board.get_grid_block_width()
        end_of_range = 1
        size_of_step_through_range = -1
        for current_row_above in range(current_row, end_of_range, size_of_step_through_range):
            for current_column in range(grid_block_width):
                game_field[current_row_above][ current_column ] = game_field[current_row_above - 1][ current_column ]
    # maybe make moves sub classes of a moves class and use poly
    