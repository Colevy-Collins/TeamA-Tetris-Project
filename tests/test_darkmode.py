import pygame
import pytest
from src.Themes import Themes
from src.DarkModeButton import DarkModeButton

@pytest.fixture
def dark_mode_button_instance():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    themes = Themes()
    font = pygame.font.Font(None, 30)
    colors = {'normal': (255, 255, 255), 'hover': (200, 200, 200), 'pressed': (150, 150, 150)}
    return DarkModeButton(screen, 'TestButton', (100, 100), (200, 50), font, colors)

def test_dark_mode_button_initialization(dark_mode_button_instance):
    assert isinstance(dark_mode_button_instance, DarkModeButton)

def test_dark_mode_button_get_text(dark_mode_button_instance):
    assert dark_mode_button_instance.getText() is "TestButton"

def test_dark_mode_button_create_text_surface(dark_mode_button_instance):
    text_surface, text_rect = dark_mode_button_instance.create_text_surface('TestText', dark_mode_button_instance.font, (255, 255, 255))
    assert isinstance(text_surface, pygame.Surface)
    assert isinstance(text_rect, pygame.Rect)

def test_dark_mode_button_change_text(dark_mode_button_instance):
    dark_mode_button_instance.changeText('NewText')
    assert dark_mode_button_instance.getText() == 'NewText'

def test_dark_mode_button_toggle_dark_mode(dark_mode_button_instance):
    initial_toggle = dark_mode_button_instance.getDarkModeToggle()
    dark_mode_button_instance.toggleDarkMode()
    assert dark_mode_button_instance.getDarkModeToggle() != initial_toggle
