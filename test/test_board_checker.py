import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.PygameDelegate import PygameDelegate
from src.TetrisBoard import TetrisBoard
from src.TetrisBoardChecker import BoardChecker

pygame = PygameDelegate()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Test for the BoardChecker class
def test_board_checker_clear_lines():

    # Test case where a single line needs to be cleared
    game_field_1 = [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
    ]
    expected_game_field_1 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 0, 1],
    ]
    tetris_board_1 = TetrisBoard()
    tetris_board_1.set_grid_block_width(4)
    tetris_board_1.set_grid_block_height(4)
    tetris_board_1.set_game_field(game_field_1)
    board_checker_1 = BoardChecker(tetris_board_1)
    
    board_checker_1.clear_lines()

    print("\nActual Game Field after clearing lines:")
    for row in tetris_board_1.get_game_field():
        print(row)

    print("\nExpected Game Field:")
    for row in expected_game_field_1:
        print(row)

    assert tetris_board_1.get_game_field() == expected_game_field_1
