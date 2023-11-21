import pygame
import pytest
from src.Themes import Themes
from src.ThemeButton import ThemeButton

@pytest.fixture
def theme_button_instance():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    themes = Themes()
    font = pygame.font.Font(None, 30)
    colors = {'normal': (255, 255, 255), 'hover': (200, 200, 200), 'pressed': (150, 150, 150)}
    return ThemeButton(screen, 'TestButton', (100, 100), (200, 50), font, colors)

def test_theme_button_initialization(theme_button_instance):
    assert isinstance(theme_button_instance, ThemeButton)

def test_theme_button_draw(theme_button_instance):
    theme_button_instance.draw()

# Add more tests as needed
