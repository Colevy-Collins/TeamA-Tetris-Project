import pytest
import pygame
from src.SoundManager import SoundManager
from unittest.mock import Mock

@pytest.fixture(scope="module", autouse=True)
def pygame_mixer_setup():
    pygame.init()
    pygame.mixer.init()
    yield
    pygame.mixer.quit()

@pytest.fixture(autouse=True)
def sound_manager(mocker):
    # Mock mixer.Sound objects and any other necessary parts of pygame
    mocker.patch('pygame.mixer.Sound', return_value=Mock())
    mocker.patch('pygame.mixer.music')

    # Create the SoundManager instance
    sm = SoundManager()
    return sm

def test_play_move_sound(sound_manager):
    sound_manager.play_move_sound()
    # Assert that the mock Sound object's `play` method was called
    pygame.mixer.Sound().play.assert_called_once()

def test_play_landing_sound(sound_manager):
    sound_manager.play_landing_sound()
    pygame.mixer.Sound().play.assert_called_once()

def test_play_clear_line_sound(sound_manager):
    sound_manager.play_clear_line_sound()
    pygame.mixer.Sound().play.assert_called_once()

def test_play_space_sound(sound_manager):
    sound_manager.play_space_sound()
    pygame.mixer.Sound().play.assert_called_once()

def test_play_game_over_sound(sound_manager):
    sound_manager.play_game_over_sound()
    pygame.mixer.Sound().play.assert_called_once()

def test_play_background_music(sound_manager):
    sound_manager.play_background_music()
    pygame.mixer.music.play.assert_called_once()

def test_stop_background_music(sound_manager):
    sound_manager.play_background_music()
    sound_manager.stop_background_music()
    pygame.mixer.music.stop.assert_called_once()