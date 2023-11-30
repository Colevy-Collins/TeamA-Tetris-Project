import pytest
from unittest.mock import patch
from src.SoundManager import SoundManager


@pytest.fixture
def sound_manager():
    with patch('pygame.mixer.init'), \
            patch('pygame.mixer.Sound'), \
            patch('pygame.mixer.music.load'), \
            patch('pygame.mixer.music.play'), \
            patch('pygame.mixer.music.stop'):
        yield SoundManager()


def test_play_move_sound(sound_manager):
    with patch.object(sound_manager.move_sound, 'play') as mock_play_move_sound:
        sound_manager.play_move_sound()
        mock_play_move_sound.assert_called_once()


def test_play_landing_sound(sound_manager):
    with patch.object(sound_manager.landing_sound, 'play') as mock_play_landing_sound:
        sound_manager.play_landing_sound()
        mock_play_landing_sound.assert_called_once()


def test_play_clear_line_sound(sound_manager):
    with patch.object(sound_manager.clear_line_sound, 'play') as mock_play_clear_line_sound:
        sound_manager.play_clear_line_sound()
        mock_play_clear_line_sound.assert_called_once()


def test_play_space_sound(sound_manager):
    with patch.object(sound_manager.space_sound, 'play') as mock_play_space_sound:
        sound_manager.play_space_sound()
        mock_play_space_sound.assert_called_once()


def test_play_background_music(sound_manager):
    with patch('pygame.mixer.music.play') as mock_play_background_music:
        sound_manager.play_background_music()
        mock_play_background_music.assert_called_once_with(-1, 0.0)


def test_stop_background_music(sound_manager):
    with patch('pygame.mixer.music.stop') as mock_stop_background_music:
        sound_manager.stop_background_music()
        mock_stop_background_music.assert_called_once()


def test_play_game_over_sound(sound_manager):
    with patch.object(sound_manager.game_over_sound, 'play') as mock_play_game_over_sound:
        sound_manager.play_game_over_sound()
        mock_play_game_over_sound.assert_called_once()
