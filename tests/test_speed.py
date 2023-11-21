import pygame
import pytest
from src.Themes import Themes
from src.TetrisButton import Button
from src.SpeedButton import SpeedButton

@pytest.fixture
def speed_button_instance():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    themes = Themes()
    font = pygame.font.Font(None, 30)
    colors = {'normal': (255, 255, 255), 'hover': (200, 200, 200), 'pressed': (150, 150, 150)}
    return SpeedButton(screen, 'TestButton', (100, 100), (200, 50), font, colors)

def test_speed_button_initialization(speed_button_instance):
    assert isinstance(speed_button_instance, SpeedButton)

def test_speed_button_draw(speed_button_instance):
    speed_button_instance.draw()

def test_speed_button_create_text_surface(speed_button_instance):
    text_surface, text_rect = speed_button_instance.create_text_surface('TestText', speed_button_instance.font, (255, 255, 255))
    assert isinstance(text_surface, pygame.Surface)
    assert isinstance(text_rect, pygame.Rect)

def test_speed_button_change_text(speed_button_instance):
    speed_button_instance.changeText('NewText')
    assert speed_button_instance.getText() == 'NewText'

# Add more tests as needed
