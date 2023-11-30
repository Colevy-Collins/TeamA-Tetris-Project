import pytest
from src.TetrisBoardManager import BoardManager
from src.TetrisBlock import TetrisBlock
from src.TetrisBoard import TetrisBoard
from src.SoundManager import SoundManager 
from src.HighScoreHandler import HighScoreHandler
from unittest.mock import patch
from unittest.mock import MagicMock

import pygame

@pytest.fixture(scope='session', autouse=True)
def pygame_mixer_init():
    pygame.mixer.init()
    pygame.mixer.set_num_channels(0)
    yield
    pygame.mixer.quit()

NUM_OF_SHAPE_GRID_ROWS = 4
NUM_OF_SHAPE_GRID_COLUMNS = 4
ACCOUNT_FOR_NEXT_ROW = 4

@pytest.fixture
def board_manager():
    tetris_block = TetrisBlock()
    tetris_board = TetrisBoard()
    sound_manager = SoundManager()
    high_score_handler = HighScoreHandler('src/data', 'high_score.txt')
    tetris_board.initialize_board(20, 10)
    manager = BoardManager(tetris_block, tetris_board, sound_manager, high_score_handler)
    return manager


def test_create_figure_no_intersection(board_manager):
    start_x = 3
    start_y = 0
    board_manager.create_figure(start_x, start_y)
    assert board_manager.tetris_block.get_shift_in_x() == start_x
    assert board_manager.tetris_block.get_shift_in_y() == start_y
    assert not board_manager.check_intersection()
    assert board_manager.get_game_state() == "start"


def test_freeze_figure(board_manager):
    board_manager.tetris_block.set_shift_in_x(5)
    board_manager.tetris_block.set_shift_in_y(18)
    board_manager.tetris_block.set_current_figure_type(6)
    board_manager.freeze_figure()
    game_field = board_manager.tetris_board.get_game_field()
    shape = board_manager.tetris_block.get_shape()
    color = board_manager.tetris_block.get_current_figure_color()
    for i in range(NUM_OF_SHAPE_GRID_ROWS):
        for j in range(NUM_OF_SHAPE_GRID_COLUMNS):
            if (i * ACCOUNT_FOR_NEXT_ROW + j) in shape:
                assert game_field[18+i][5+j] == color

def test_check_intersection(board_manager):
    board_manager.tetris_block.set_shift_in_x(5)
    board_manager.tetris_block.set_shift_in_y(18)
    board_manager.tetris_block.set_current_figure_type(6)
    board_manager.freeze_figure()
    board_manager.tetris_block.set_shift_in_y(20)
    assert board_manager.check_intersection()

def test_move_to_bottom(board_manager):
    start_x = 3
    start_y = 0
    board_manager.create_figure(start_x, start_y)
    initial_y = board_manager.tetris_block.get_shift_in_y()
    with patch.object(board_manager, 'game_rules', return_value=None):
        board_manager.move_to_bottom()
    new_y = board_manager.tetris_block.get_shift_in_y()
    assert new_y > initial_y
    board_manager.tetris_block.set_shift_in_y(new_y + 1)
    assert board_manager.check_intersection()


def test_rotate_figure(board_manager):
    initial_rotation = board_manager.tetris_block.get_current_rotation()
    board_manager.rotate_figure()
    expected_rotation = (initial_rotation + 1) % len(board_manager.tetris_block.get_figure())
    assert board_manager.tetris_block.get_current_rotation() == expected_rotation

def test_increase_score(board_manager):
    board_manager.high_score_handler.read_data = MagicMock(return_value=0)
    board_manager.high_score_handler.write_data = MagicMock()
    board_manager.set_score(0)
    board_manager.increase_score()
    score_increment = 2
    expected_score = 0 + score_increment
    actual_score = board_manager.get_score()
    assert actual_score == expected_score, f"Expected score to be {expected_score}, but got {actual_score}."

def test_game_state_set_and_get(board_manager):
    board_manager.set_game_state("start")
    assert board_manager.get_game_state() == "start"
    board_manager.set_game_state("gameover")
    assert board_manager.get_game_state() == "gameover"
    board_manager.set_game_state("invalid_state")
    assert board_manager.get_game_state() == "gameover"