import pytest
from unittest.mock import MagicMock, patch
from src.TetrisStartMenu import TetrisStartMenu
import asyncio
import pygame

@pytest.mark.asyncio
async def test_menu_ui_appearance():
    start_menu = TetrisStartMenu()
    with patch.object(start_menu, 'initialize', side_effect=lambda: asyncio.sleep(0)):
        with patch('pygame.event.get', MagicMock(return_value=[MagicMock(type=pygame.QUIT)])):
            task = asyncio.create_task(start_menu.initialize())
            await asyncio.sleep(1)
            task.cancel()


@pytest.mark.asyncio
async def test_menu_start_button():
    start_menu = TetrisStartMenu()
    with patch.object(start_menu.start_button, 'clickCheck', MagicMock(return_value=True)):
        async def simulate_start_button():
            await asyncio.sleep(0)
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN
            start_menu.buttonHandle([mock_event])
            assert start_menu.running == False
        await simulate_start_button()

@pytest.mark.asyncio
async def test_menu_quit_button():
    start_menu = TetrisStartMenu()
    with patch.object(start_menu.quit_button, 'clickCheck', MagicMock(return_value=True)):
        start_menu.running = False
        async def simulate_quit_button():
            await asyncio.sleep(0)
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN
            with pytest.raises(SystemExit) as exc_info:
                start_menu.buttonHandle([mock_event])
            assert exc_info.type == SystemExit
        await simulate_quit_button()
