import pytest
from src.TetrisBoardManager import BoardManager
from src.TetrisBlock import TetrisBlock
from src.TetrisBoard import TetrisBoard
from src.SoundManager import SoundManager 
from src.HighScoreHandler import HighScoreHandler
from unittest.mock import patch

import pygame
pygame.mixer.init()  # This initializes the mixer, but we want to avoid actual sound playback
pygame.mixer.set_num_channels(0)  # This effectively mutes the mixer by setting the number of channels to zero.

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
    # Assert that no intersection occurred and game state remains 'start'
    assert not board_manager.check_intersection()
    assert board_manager.get_game_state() == "start"


def test_freeze_figure(board_manager):
    # Pre-set the block at a specific place where the freeze will happen
    board_manager.tetris_block.set_shift_in_x(5)
    board_manager.tetris_block.set_shift_in_y(18)
    board_manager.tetris_block.set_current_figure_type(6)  # Assuming this sets a specific block type
    board_manager.freeze_figure()
    # Now assert that the block's position in the game_field reflect the freeze
    game_field = board_manager.tetris_board.get_game_field()
    shape = board_manager.tetris_block.get_shape()
    color = board_manager.tetris_block.get_current_figure_color()
    for i in range(NUM_OF_SHAPE_GRID_ROWS):
        for j in range(NUM_OF_SHAPE_GRID_COLUMNS):
            if (i * ACCOUNT_FOR_NEXT_ROW + j) in shape:
                assert game_field[18+i][5+j] == color  # Assert each block part is now part of game_field


def test_check_intersection(board_manager):
    # Set up board and block in a way that will cause an intersection
    # For example, place a block at the bottom and try to move it down
    board_manager.tetris_block.set_shift_in_x(5)
    board_manager.tetris_block.set_shift_in_y(18)
    board_manager.tetris_block.set_current_figure_type(6)
    # Calling freeze_figure to place the block on the game board
    board_manager.freeze_figure()
    # Moving the tetris_block down should now cause an intersection
    board_manager.tetris_block.set_shift_in_y(20)
    assert board_manager.check_intersection()  # Expecting True


def test_move_to_bottom(board_manager):
    start_x = 3
    start_y = 0
    board_manager.create_figure(start_x, start_y)
    initial_y = board_manager.tetris_block.get_shift_in_y()

    # Patch the game_rules method to not execute during the test
    with patch.object(board_manager, 'game_rules', return_value=None):
        board_manager.move_to_bottom()

    # Assert the new Y is at the bottom of the board and greater than initial Y
    new_y = board_manager.tetris_block.get_shift_in_y()
    assert new_y > initial_y
    # Now you can assert that the next move down would cause an intersection
    board_manager.tetris_block.set_shift_in_y(new_y + 1)
    assert board_manager.check_intersection()


def test_rotate_figure(board_manager):
    initial_rotation = board_manager.tetris_block.get_current_rotation()
    board_manager.rotate_figure()
    # Assuming rotations just increment and loop back to 0
    expected_rotation = (initial_rotation + 1) % len(board_manager.tetris_block.get_figure())
    assert board_manager.tetris_block.get_current_rotation() == expected_rotation
    # You would create additional assertions if an intersection causes the rotation to revert


def test_increase_score(board_manager):
    # Mock the high score handler's read_data method to always return 0
    with patch.object(board_manager.high_score_handler, 'read_data', return_value=0):
        initial_score = board_manager.get_score()
        
        # Call the increase_score method, which supposedly increases the score
        board_manager.increase_score()
        score_increment = 2  # or use the actual increment value set in the increase_score method
        
        # Assert the score is increased accordingly
        assert board_manager.get_score() == initial_score + score_increment

        # Since we mocked the high_score_handler to return 0,
        # the new high score should be set to the increased score
        assert board_manager.get_high_score() == initial_score + score_increment

def test_game_state_set_and_get(board_manager):
    # Set the game state and assert it changes appropriately
    board_manager.set_game_state("start")
    assert board_manager.get_game_state() == "start"
    board_manager.set_game_state("gameover")
    assert board_manager.get_game_state() == "gameover"
    # Attempt to set an invalid state and assert the game state defaults to "gameover"
    board_manager.set_game_state("invalid_state")
    assert board_manager.get_game_state() == "gameover"