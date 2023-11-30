import pytest
import pygame
from unittest.mock import Mock
from src.TetrisBoard import TetrisBoard

@pytest.fixture
def tetris_board():
    return TetrisBoard()

def test_tetris_board_init(tetris_board):
    assert tetris_board.size_of_grid_block == 20
    assert tetris_board.start_x_position == 100
    assert tetris_board.start_y_position == 60
    assert tetris_board.grid_block_height == 0
    assert tetris_board.grid_block_width == 0
    assert tetris_board.window_size == (400, 500)
    assert tetris_board.game_field == []
    assert isinstance(tetris_board.colors, tuple)
    assert tetris_board.board_color == (255, 255, 255)

def test_initialize_board(tetris_board):
    height = 20
    width = 10
    tetris_board.initialize_board(height, width)
    assert tetris_board.get_grid_block_height() == height
    assert tetris_board.get_grid_block_width() == width
    assert len(tetris_board.get_game_field()) == height
    for row in tetris_board.get_game_field():
        assert len(row) == width

def test_switch_board_color(tetris_board):
    tetris_board.set_board_color((0, 0, 0,))
    tetris_board.switch_board_color()
    assert tetris_board.get_board_color() == (255, 255, 255)
    tetris_board.switch_board_color()
    assert tetris_board.get_board_color() == (0, 0, 0)

def test_draw_game_board(tetris_board):
    tetris_board.initialize_board(20, 10)
    mock_screen = Mock()
    pygame.draw.rect = Mock()
    tetris_board.draw_game_board(mock_screen)
    assert pygame.draw.rect.called