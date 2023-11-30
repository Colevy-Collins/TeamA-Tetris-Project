import pytest
from unittest.mock import MagicMock, patch, Mock
from src.TetrisPauseMenu import PausedMenu
from src.TetrisPauseIcon import PauseIconButton
import asyncio
import pygame


@pytest.mark.asyncio
async def test_pause_icon_button():
    # Create an instance of PauseIconButton
    pause_icon_button = PauseIconButton(MagicMock(), (0, 0), [40, 40, 40], [(150, 150, 150), (255, 255, 255)])

    # Mock the behavior of draw method
    with patch.object(pause_icon_button, 'draw') as mock_draw:
        # Call initialize method
        pause_icon_button.initialize()

        # Assert that draw method was called
        mock_draw.assert_called_once()
        

# Your test function
@pytest.mark.asyncio
async def test_menu_ui_appearance():
    # Create an instance of PausedMenu
    pause_menu = PausedMenu()

    # Mock the behavior of the initialize method to avoid an infinite loop
    with patch.object(pause_menu, 'initialize', side_effect=lambda: asyncio.sleep(0)):
        # Mock pygame.event.get to return a list containing pygame.QUIT event
        with patch('pygame.event.get', MagicMock(return_value=[MagicMock(type=pygame.QUIT)])):
            # Create a task to run the mocked initialize method
            task = asyncio.create_task(pause_menu.initialize())

            # Wait for the task to finish
            await asyncio.sleep(1)

            # Cancel the task
            task.cancel()


@pytest.mark.asyncio
async def test_menu_Resume_button():
    # Create an instance of PausedMenu
    pause_menu = PausedMenu()

    # Mock the behavior of the start button
    with patch.object(pause_menu.resume_button, 'clickCheck', MagicMock(return_value=True)):
        # Simulate clicking the resume button by calling buttonHandle with a mock event
        async def simulate_resume_button():
            await asyncio.sleep(0)  # Ensure the event loop runs

            # Mock event data for a mouse button down event at position (x, y)
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN

            # Call buttonHandle with the mock event
            pause_menu.buttonHandle([mock_event])
            assert pause_menu.running == False

        # Run the simulate_resume_button coroutine
        await simulate_resume_button()

@pytest.mark.asyncio
async def test_menu_MainMenu_button():
    # Create an instance of PausedMenu
    pause_menu = PausedMenu()

    # Mock the behavior of the start button
    with patch.object(pause_menu.main_menu_button, 'clickCheck', MagicMock(return_value=True)):
        # Simulate clicking the main menu button by calling buttonHandle with a mock event
        async def simulate_mainMenu_button():
            await asyncio.sleep(0)  # Ensure the event loop runs

            # Mock event data for a mouse button down event at position (x, y)
            mock_event = MagicMock()
            mock_event.type = pygame.MOUSEBUTTONDOWN

            # Call buttonHandle with the mock event
            pause_menu.buttonHandle([mock_event])
            assert pause_menu.running == False

        # Run the simulate_mainMenu_button coroutine
        await simulate_mainMenu_button()