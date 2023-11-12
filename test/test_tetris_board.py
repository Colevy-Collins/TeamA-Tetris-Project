# test_tetris_board.py

import sys
import os
from unittest.mock import Mock

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.PygameDelegate import PygameDelegate
from src.TetrisBoard import TetrisBoard

pygame = PygameDelegate()

def test_initialize_board():
    tetris_board = TetrisBoard()
    tetris_board.initialize_board(10, 10)
    assert tetris_board.get_grid_block_height() == 10
    assert tetris_board.get_grid_block_width() == 10
    assert tetris_board.get_game_field() == [[0] * 10 for _ in range(10)]

def test_draw_game_board_integration():
    pygame.init()
    screen = pygame.display.set_mode((400, 500))

    try:
        tetris_board = TetrisBoard()
        tetris_board.initialize_board(5, 5)

        tetris_board.draw_game_board(screen)

        # Example: Assert that the top-left pixel has the expected color
        expected_color = (255, 255, 255)  # White color
        actual_color = screen.get_at((0, 0))[:3]  # Get RGB values
        assert actual_color == expected_color

        # You might add more assertions based on what you expect to see on the screen
        pygame.display.flip()  # Update the display
        pygame.time.delay(1000)  # Pause for a moment to see the result
    finally:
        pygame.quit()

def test_size_of_grid_block():
    tetris_board = TetrisBoard()
    tetris_board.set_size_of_grid_block(30)
    assert tetris_board.get_size_of_grid_block() == 30

def test_start_x_position():
    tetris_board = TetrisBoard()
    tetris_board.set_start_x_position(150)
    assert tetris_board.get_start_x_position() == 150

def test_start_y_position():
    tetris_board = TetrisBoard()
    tetris_board.set_start_y_position(100)
    assert tetris_board.get_start_y_position() == 100

def test_grid_block_height():
    tetris_board = TetrisBoard()
    tetris_board.set_grid_block_height(15)
    assert tetris_board.get_grid_block_height() == 15

def test_grid_block_width():
    tetris_board = TetrisBoard()
    tetris_board.set_grid_block_width(12)
    assert tetris_board.get_grid_block_width() == 12

def test_window_size():
    tetris_board = TetrisBoard()
    tetris_board.set_window_size((800, 600))
    assert tetris_board.get_window_size() == (800, 600)

def test_game_field():
    tetris_board = TetrisBoard()
    tetris_board.set_game_field([[1, 2, 3], [4, 5, 6]])
    assert tetris_board.get_game_field() == [[1, 2, 3], [4, 5, 6]]

def test_colors():
    tetris_board = TetrisBoard()
    tetris_board.set_colors([(0, 0, 0), (255, 255, 255)])
    assert tetris_board.get_colors() == [(0, 0, 0), (255, 255, 255)]
