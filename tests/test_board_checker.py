import pytest
from src.TetrisBoard import TetrisBoard
from src.TetrisBoardManager import BoardManager
from src.TetrisBoardChecker import BoardChecker
from src.TetrisBlock import TetrisBlock
from src.SoundManager import SoundManager  
from src.HighScoreHandler import HighScoreHandler 

import pygame
pygame.mixer.init()  # This initializes the mixer, but we want to avoid actual sound playback
pygame.mixer.set_num_channels(0)  # This effectively mutes the mixer by setting the number of channels to zero.


@pytest.fixture
def board_checker():
    tetris_block = TetrisBlock()
    tetris_board = TetrisBoard()
    sound_manager = SoundManager()
    high_score_handler = HighScoreHandler('src/data', 'high_score.txt')
    # Assume SoundManagerMock and HighScoreHandlerMock are mock versions developed for testing purposes.

    # Initialize empty board
    tetris_board.initialize_board(20, 10)

    board_manager = BoardManager(tetris_block, tetris_board, sound_manager, high_score_handler)
    checker = BoardChecker(tetris_board, board_manager, sound_manager)

    return checker

def test_clear_lines_no_full_rows(board_checker):
    # Ensure no rows are filled, so no lines are cleared
    board_checker.clear_lines()
    game_field = board_checker.tetris_board.get_game_field()
    # Assert that the game field is still empty as no lines should be cleared
    assert all(all(cell == 0 for cell in row) for row in game_field)
    # Assuming that there is a method in sound_manager to check if a sound was played
    assert not board_checker.sound_manager.was_played('clear_line_sound')  # Mock or logging assertion

def test_clear_lines_with_full_rows(board_checker):
    # Fill a row in the game field directly to simulate a full row
    game_field = board_checker.tetris_board.get_game_field()
    game_field[10] = [1] * 10  # Set row 10 as filled

    # Assume the board manager has a method to report score and it changes when a line is cleared
    initial_score = board_checker.board_manager.get_score()
    board_checker.clear_lines()
    assert board_checker.board_manager.get_score() > initial_score
    # Assert that row is no longer filled after clear_lines
    assert 0 in game_field[10]
    # Assert the sound was played
    assert board_checker.sound_manager.was_played('clear_line_sound')  # Mock or logging assertion

def test_check_if_row_is_filled(board_checker):
    # Fill a row in the game field directly to simulate a full row
    game_field = board_checker.tetris_board.get_game_field()
    game_field[10] = [1] * 10  # Set row 10 as filled
    assert board_checker.check_if_row_is_filled(10)

    # Empty one cell and ensure it reports the row is not filled
    game_field[10][0] = 0
    assert not board_checker.check_if_row_is_filled(10)

def test_delete_row(board_checker):
    # Fill a row in the game field
    game_field = board_checker.tetris_board.get_game_field()
    game_field[10] = [1] * 10
    game_field[9] = [2] * 10

    board_checker.delete_row(10)
    
    # Assert that row 10 now contains the values from row 9, and row 9 is empty except for boundary
    assert game_field[10] == [2] * 10
    assert game_field[9] == [0] * 10  # Assuming a new empty row added on top after deletion