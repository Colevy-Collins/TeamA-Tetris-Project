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
    pygame.mixer.init()
    pygame.mixer.set_num_channels(0)
    yield
    pygame.mixer.quit()
    

class MockSoundManager:
    def __init__(self):
        self.played_sounds = {}
        for method in ["play_move_sound", "play_landing_sound", "play_clear_line_sound", "play_space_sound", "play_game_over_sound"]:
            setattr(self, method, MagicMock(side_effect=self._record_play(method)))

    def _record_play(self, sound_name):
        def record(*args, **kwargs):
            self.played_sounds[sound_name] = True
        return record

    def was_played(self, sound_name):
        return self.played_sounds.get(sound_name, False)

    def play_background_music(self):
        pass

    def stop_background_music(self):
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
    checker.clear_lines()
    game_field = checker.tetris_board.get_game_field()
    assert all(all(cell == 0 for cell in row) for row in game_field)

def test_clear_lines_with_full_rows(board_checker):
    checker, mock_play_clear_line_sound = board_checker
    checker.tetris_board.set_game_field([[0]*10]*19 + [[1]*10])
    filled_row_index = 19
    assert all(checker.tetris_board.get_game_field()[filled_row_index])
    checker.clear_lines()
    mock_play_clear_line_sound.assert_called_once()
    for row in checker.tetris_board.get_game_field():
        assert not all(row)

def test_check_if_row_is_filled(board_checker):
    checker, mock_play_clear_line_sound = board_checker 
    game_field = checker.tetris_board.get_game_field()
    game_field[10] = [1] * 10
    assert checker.check_if_row_is_filled(10)
    game_field[10][0] = 0
    assert not checker.check_if_row_is_filled(10)

def test_delete_row(board_checker):
    checker, mock_play_clear_line_sound = board_checker 
    game_field = checker.tetris_board.get_game_field()
    game_field[10] = [1] * 10
    game_field[9] = [2] * 10

    checker.delete_row(10)
    assert game_field[10] == [2] * 10
    assert game_field[9] == [0] * 10 