import pytest
from unittest.mock import MagicMock, patch, Mock
from src.TetrisPauseMenu import PausedMenu
from src.TetrisPauseIcon import PauseIconButton
import asyncio
import pygame


@pytest.mark.asyncio
async def test_pause_icon_button():
    pause_icon_button = PauseIconButton(MagicMock(), (0, 0), [40, 40, 40], [(150, 150, 150), (255, 255, 255)])
    with patch.object(pause_icon_button, 'draw') as mock_draw:
        pause_icon_button.initialize()
        mock_draw.assert_called_once()
        
@pytest.mark.asyncio
async def test_menu_ui_appearance():
    pause_menu = PausedMenu()
    with patch.object(pause_menu, 'initialize', side_effect=lambda: asyncio.sleep(0)):
        with patch('pygame.event.get', MagicMock(return_value=[MagicMock(type=pygame.QUIT)])):
            task = asyncio.create_task(pause_menu.initialize())
            await asyncio.sleep(1)
            task.cancel()

@pytest.mark.asyncio
async def test_menu_Resume_button():
    pause_menu = PausedMenu()
    with patch.object(pause_menu.resume_button, 'clickCheck', MagicMock(return_value=True)):
        async def simulate_resume_button():
            await asyncio.sleep(0)
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN
            pause_menu.buttonHandle([mock_event])
            assert pause_menu.running == False
        await simulate_resume_button()

@pytest.mark.asyncio
async def test_menu_MainMenu_button():
    pause_menu = PausedMenu()
    with patch.object(pause_menu.main_menu_button, 'clickCheck', MagicMock(return_value=True)):
        async def simulate_mainMenu_button():
            await asyncio.sleep(0)
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN
            pause_menu.buttonHandle([mock_event])
            assert pause_menu.running == False
        await simulate_mainMenu_button()