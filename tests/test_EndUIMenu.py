import pytest
from unittest.mock import MagicMock, patch
from src.TetrisEndMenu import EndGameMenu
from tetris_verFinal import main
import asyncio
import pygame

@pytest.mark.asyncio
async def test_draw_score_called():
    mock_board_manager = MagicMock()
    end_menu = EndGameMenu(mock_board_manager)
    end_menu.draw_score(mock_board_manager)
    assert mock_board_manager.get_score.called

@pytest.mark.asyncio
async def test_draw_high_score_called():
    mock_board_manager = MagicMock()
    end_menu = EndGameMenu(mock_board_manager)
    end_menu.draw_high_score(mock_board_manager)
    assert mock_board_manager.get_high_score.called

@pytest.mark.asyncio
async def test_end_ui_appearance():
    mock_board_manager = MagicMock()
    end_menu = EndGameMenu(mock_board_manager)
    with patch.object(end_menu, 'initialize', side_effect=lambda: asyncio.sleep(0)):
        with patch('pygame.event.get', MagicMock(return_value=[MagicMock(type=pygame.QUIT)])):
            task = asyncio.create_task(end_menu.initialize())
            await asyncio.sleep(1)
            task.cancel()


@pytest.mark.asyncio
async def test_main_menu_button():
    mock_board_manager = MagicMock()
    end_menu = EndGameMenu(mock_board_manager)
    with patch.object(end_menu.main_menu_button, 'clickCheck', MagicMock(return_value=True)):
        async def simulate_main_menu_button():
            await asyncio.sleep(0)
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN
            end_menu.buttonHandle([mock_event])
            assert end_menu.running == False
        await simulate_main_menu_button()

@pytest.mark.asyncio
async def test_menu_quit_button():
    mock_board_manager = MagicMock()
    end_menu = EndGameMenu(mock_board_manager)
    with patch.object(end_menu.quit_button, 'clickCheck', MagicMock(return_value=True)):
        end_menu.running = False
        async def simulate_quit_button():
            await asyncio.sleep(0)
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN
            with pytest.raises(SystemExit) as exc_info:
                end_menu.buttonHandle([mock_event])
            assert exc_info.type == SystemExit
        await simulate_quit_button()