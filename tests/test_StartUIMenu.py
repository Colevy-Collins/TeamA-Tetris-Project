import pytest
from unittest.mock import patch
from src.TetrisStartMenu import TetrisStartMenu

# Mocking pygame for testing
pygame_mock = patch("src.TetrisStartMenu.pygame", autospec=True).start()

# Mocking PygameDelegate and PygameDelegate.init()
pygame_mock.PygameDelegate.return_value.init.return_value = None

# Mocking the start button clickCheck method
@pytest.fixture
def start_menu():
    with patch("src.TetrisUIButton.UIButton") as mock_ui_button:
        mock_ui_button.return_value.clickCheck.return_value = True
        return TetrisStartMenu()

def test_start_menu_ui(start_menu):
    assert start_menu.running is True

    with patch("src.TetrisStartMenu.pygame.display.flip") as mock_flip:
        start_menu.initialize()

    mock_flip.assert_called_once()

    assert start_menu.start_button.draw.called
    assert start_menu.quit_button.draw.called
    assert start_menu.start_button.clickCheck.called
    assert start_menu.quit_button.clickCheck.called

    # Add more assertions based on your specific requirements
