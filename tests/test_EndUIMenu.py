import pytest
from unittest.mock import MagicMock, patch
from src.TetrisEndMenu import EndGameMenu
from tetris_verFinal import main
import asyncio
import pygame

@pytest.mark.asyncio
async def test_draw_score_called():
    # Mock the board_manager
    mock_board_manager = MagicMock()

    # Create an instance of EndGameMenu with the mocked board_manager
    end_menu = EndGameMenu(mock_board_manager)

    # Call the draw_score method
    end_menu.draw_score(mock_board_manager)

    # Check if draw_score is called
    assert mock_board_manager.get_score.called

@pytest.mark.asyncio
async def test_draw_high_score_called():
    # Mock the board_manager
    mock_board_manager = MagicMock()

    # Create an instance of EndGameMenu with the mocked board_manager
    end_menu = EndGameMenu(mock_board_manager)

    # Call the draw_high_score method
    end_menu.draw_high_score(mock_board_manager)

    # Check if draw_high_score is called
    assert mock_board_manager.get_high_score.called



# Your test function
@pytest.mark.asyncio
async def test_end_ui_appearance():
    # Mock the board_manager
    mock_board_manager = MagicMock()
    
    # Create an instance of EndGameMenu with the mocked board_manager
    end_menu = EndGameMenu(mock_board_manager)

    # Mock the behavior of the initialize method to avoid an infinite loop
    with patch.object(end_menu, 'initialize', side_effect=lambda: asyncio.sleep(0)):
        # Mock pygame.event.get to return a list containing pygame.QUIT event
        with patch('pygame.event.get', MagicMock(return_value=[MagicMock(type=pygame.QUIT)])):
            # Create a task to run the mocked initialize method
            task = asyncio.create_task(end_menu.initialize())

            # Wait for the task to finish
            await asyncio.sleep(1)

            # Cancel the task
            task.cancel()


@pytest.mark.asyncio
async def test_main_menu_button():
    # Mock the board_manager
    mock_board_manager = MagicMock()

    # Create an instance of EndGameMenu with the mocked board_manager
    end_menu = EndGameMenu(mock_board_manager)

    # Mock the behavior of the main menu button
    with patch.object(end_menu.main_menu_button, 'clickCheck', MagicMock(return_value=True)):
        # Simulate clicking the main menu button by calling buttonHandle with a mock event
        async def simulate_main_menu_button():
            await asyncio.sleep(0)  # Ensure the event loop runs

            # Mock event data for a mouse button down event at position (x, y)
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN

            # Call buttonHandle with the mock event
            end_menu.buttonHandle([mock_event])
            assert end_menu.running == False

        # Run the simulate_main_menu_button coroutine
        await simulate_main_menu_button()

@pytest.mark.asyncio
async def test_menu_quit_button():
    # Mock the board_manager
    mock_board_manager = MagicMock()

    # Create an instance of EndGameMenu with the mocked board_manager
    end_menu = EndGameMenu(mock_board_manager)

    # Mock the behavior of the quit button to raise SystemExit
    with patch.object(end_menu.quit_button, 'clickCheck', MagicMock(return_value=True)):
        # Set running to False to break out of the infinite loop
        end_menu.running = False

        # Simulate clicking the quit button by calling buttonHandle with a mock event
        async def simulate_quit_button():
            await asyncio.sleep(0)  # Ensure the event loop runs

            # Mock event data for a mouse button down event at position (x, y)
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN

            # Call buttonHandle with the mock event
            with pytest.raises(SystemExit) as exc_info:
                end_menu.buttonHandle([mock_event])

            # Check if the raised exception is SystemExit
            assert exc_info.type == SystemExit

        # Run the simulate_quit_button coroutine
        await simulate_quit_button()