import pytest
from unittest.mock import patch, MagicMock
from src.TetrisBoard import TetrisBoard
from src.TetrisBoardManager import BoardManager
from src.TetrisBoardChecker import BoardChecker
from src.TetrisBlock import TetrisBlock
from src.HighScoreHandler import HighScoreHandler
from src.SoundManager import SoundManager
import pygame

@pytest.fixture(scope='session', autouse=True)
def pygame_mixer_init():
    # Initialize pygame mixer
    pygame.mixer.init()
    # Set the number of channels to 0 to "mute" the mixer
    pygame.mixer.set_num_channels(0)
    yield
    # Quit pygame mixer after all tests are done
    pygame.mixer.quit()
    

# Mock SoundManager for tests
class MockSoundManager:
    def __init__(self):
        # Track played sounds
        self.played_sounds = {}
        # Every sound method should be added here
        for method in ["play_move_sound", "play_landing_sound", "play_clear_line_sound", "play_space_sound", "play_game_over_sound"]:
            setattr(self, method, MagicMock(side_effect=self._record_play(method)))

    def _record_play(self, sound_name):
        def record(*args, **kwargs):
            self.played_sounds[sound_name] = True
        return record

    def was_played(self, sound_name):
        # Check if the sound has been played
        return self.played_sounds.get(sound_name, False)

    def play_background_music(self):
        # Mock background music method
        pass

    def stop_background_music(self):
        # Mock stop background music method
        pass

@pytest.fixture
def board_checker():
    with patch('src.SoundManager.SoundManager.play_clear_line_sound') as mock_play_clear_line_sound:
        tetris_block = TetrisBlock()
        tetris_board = TetrisBoard()
        sound_manager = SoundManager()  # Initialize the actual SoundManager
        high_score_handler = HighScoreHandler('src/data', 'high_score.txt')

        tetris_board.initialize_board(20, 10)
        board_manager = BoardManager(tetris_block, tetris_board, sound_manager, high_score_handler)
        board_manager.sound_manager.play_clear_line_sound = mock_play_clear_line_sound  # Replace with mock method
        checker = BoardChecker(tetris_board, board_manager, sound_manager)

        yield checker, mock_play_clear_line_sound

def test_clear_lines_no_full_rows(board_checker):
    checker, mock_play_clear_line_sound = board_checker 
    # Ensure no rows are filled, so no lines are cleared
    checker.clear_lines()
    game_field = checker.tetris_board.get_game_field()
    # Assert that the game field is still empty as no lines should be cleared
    assert all(all(cell == 0 for cell in row) for row in game_field)

def test_clear_lines_with_full_rows(board_checker):
    checker, mock_play_clear_line_sound = board_checker

    # Fill the last row to simulate a full row (assuming 0-indexed and board has size 20x10)
    checker.tetris_board.set_game_field([[0]*10]*19 + [[1]*10])

    # Check if at least one line is filled before clearing
    filled_row_index = 19  # Last row in a 0-indexed grid
    assert all(checker.tetris_board.get_game_field()[filled_row_index])

    # Call the method to clear lines
    checker.clear_lines()

    # Assert that the clear line sound was played
    mock_play_clear_line_sound.assert_called_once()

    # After clearing, assert that the filled row is gone
    # We need to check all rows above the filled row index because they collapse down
    for row in checker.tetris_board.get_game_field():
        assert not all(row)  # No row should be completely filled

def test_check_if_row_is_filled(board_checker):
    checker, mock_play_clear_line_sound = board_checker 
    # Fill a row in the game field directly to simulate a full row
    game_field = checker.tetris_board.get_game_field()
    game_field[10] = [1] * 10  # Set row 10 as filled
    assert checker.check_if_row_is_filled(10)

    # Empty one cell and ensure it reports the row is not filled
    game_field[10][0] = 0
    assert not checker.check_if_row_is_filled(10)

def test_delete_row(board_checker):
    checker, mock_play_clear_line_sound = board_checker 
    # Fill a row in the game field
    game_field = checker.tetris_board.get_game_field()
    game_field[10] = [1] * 10
    game_field[9] = [2] * 10

    checker.delete_row(10)
    
    # Assert that row 10 now contains the values from row 9, and row 9 is empty except for boundary
    assert game_field[10] == [2] * 10
    assert game_field[9] == [0] * 10  # Assuming a new empty row added on top after deletion