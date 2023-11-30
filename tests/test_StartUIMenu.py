import pytest
from unittest.mock import MagicMock, patch
from src.TetrisStartMenu import TetrisStartMenu
import asyncio
import pygame
"""
@pytest.mark.asyncio
async def test_menu_ui_appearance():
    # Create an instance of TetrisStartMenu
    start_menu = TetrisStartMenu()

    # Create a task to run the initialize method
    task = asyncio.create_task(start_menu.initialize())
    await asyncio.sleep(1)

    assert start_menu.startGameFlag == False

    # Stop the UI
    start_menu.stop_ui()

    # Cancel the task
    task.cancel()

    # Wait for the task to be cancelled
    with pytest.raises(asyncio.CancelledError):
        await task

    # Delete the start_menu object
    start_menu = None
"""

@pytest.mark.asyncio
async def test_menu_start_button():
    # Create an instance of TetrisStartMenu
    start_menu = TetrisStartMenu()

    # Mock the behavior of the start button
    with patch.object(start_menu.start_button, 'clickCheck', MagicMock(return_value=True)):
        # Simulate clicking the start button by calling buttonHandle with a mock event
        async def simulate_start_button():
            await asyncio.sleep(0)  # Ensure the event loop runs

            # Mock event data for a mouse button down event at position (x, y)
            x, y = 200, 305
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN
            mock_event.pos = (x, y)

            # Call buttonHandle with the mock event
            start_menu.buttonHandle([mock_event])

        # Run the simulate_start_button coroutine
        await simulate_start_button()

@pytest.mark.asyncio
async def test_menu_quit_button():
    # Create an instance of TetrisStartMenu
    start_menu = TetrisStartMenu()

    # Mock the behavior of the quit button to raise SystemExit
    with patch.object(start_menu.quit_button, 'clickCheck', MagicMock(return_value=True)):
        # Set running to False to break out of the infinite loop
        start_menu.running = False

        # Simulate clicking the quit button by calling buttonHandle with a mock event
        async def simulate_quit_button():
            await asyncio.sleep(0)  # Ensure the event loop runs

            # Mock event data for a mouse button down event at position (x, y)
            x, y = 200, 370
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN
            mock_event.pos = (x, y)

            # Call buttonHandle with the mock event
            with pytest.raises(SystemExit) as exc_info:
                start_menu.buttonHandle([mock_event])

            # Check if the raised exception is SystemExit
            assert exc_info.type == SystemExit

        # Run the simulate_quit_button coroutine
        await simulate_quit_button()
