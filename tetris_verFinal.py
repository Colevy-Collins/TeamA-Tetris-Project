from src.PygameDelegate import PygameDelegate
from src.Button import Button
from src.TetrisBoard import TetrisBoard
from src.TetrisBlock import TetrisBlock
from src.TetrisBoardManager import BoardManager
from src.TetrisBoardChecker import BoardChecker
from src.TetrisStartMenu import TetrisStartMenu
from src.TetrisEndMenu import EndGameMenu
from src.TetrisPauseMenu import PausedMenu
from src.TetrisPauseIcon import PauseIconButton
from src.Difficulty import Difficulty
#from src.TetrisUIButton import TextButton
from src.Themes import Themes
from src.SoundManager import SoundManager
from src.HighScoreHandler import HighScoreHandler
from src.DarkModeButton import DarkModeButton
from src.TetrisPauseIcon import PauseIconButton
from src.ThemeButton import ThemeButton
from src.SpeedButton import SpeedButton

pygame = PygameDelegate()

def main():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    themes = Themes()
    pygame.init()

    # Pygame related init
    tetris_block = TetrisBlock()
    tetris_board = TetrisBoard()
    sound_manager = SoundManager()
    high_score_handler = HighScoreHandler('src/data', 'high_score.txt')
    board_manager = BoardManager(tetris_block, tetris_board, sound_manager, high_score_handler)
    board_checker = BoardChecker(tetris_board, board_manager, sound_manager)

    # Set up the drawing window
    screen = pygame.display.set_mode(board_manager.get_window_size())
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    # Play music
    sound_manager.play_background_music()

    # we need pressing_down, fps, and counter to move_down() the Tetris Figure
    fps = 200
    counter = 0
    pressing_down = False

    #Below 2 variables used in application loop
    game_block_height = 20
    game_block_width = 10
    
    tetris_board.initialize_board(game_block_height, game_block_width)


    starting_shift_x = 3 
    starting_shift_y = 0

    board_manager.create_figure(starting_shift_x, starting_shift_y)
    gameActive = True
    level = 1
    interval = 100000

    # Controls how fast auto move occurs
    difficulty = Difficulty.CreateDifficulty()

    event_key_action_list = {
        pygame.K_UP: lambda: board_manager.rotate_figure(),
        pygame.K_DOWN: "true",
        pygame.K_LEFT: lambda: board_manager.move_sideways(-1),
        pygame.K_RIGHT: lambda: board_manager.move_sideways(1),
        pygame.K_SPACE: lambda: board_manager.move_to_bottom(),
        pygame.K_1: lambda: difficulty.increaseFallSpeed(),
        pygame.K_2: lambda: difficulty.decreaseFallSpeed()
    }

    #Button parameter creation
    sizeValues = [40, 40, 40] # button sizeX, button sizeY, Icon Size
    pausebuttonLocationX = 10
    pausebuttonLocationY = 10
    darkModeButtonLocationX = 10
    darkModeButtonLocationY = 80
    themeButtonLocationX = 10
    themeButtonLocationY = 130
    speedButtonLocationX = 315
    speedButtonLocationY = 10
    pauseIconButton = PauseIconButton(screen, (pausebuttonLocationX, pausebuttonLocationY), sizeValues, [(150, 150, 150), (255, 255, 255)])
    darkModeButton = DarkModeButton(screen, "Dark", (darkModeButtonLocationX , darkModeButtonLocationY), (60, 30), pygame.font.Font(None, 22), [themes.getWhite(), themes.getGray()])
    themeButton = ThemeButton(screen, "Theme", (themeButtonLocationX, themeButtonLocationY), (60, 30), pygame.font.Font(None, 16), [themes.getWhite(), themes.getGray()])
    speedButton = SpeedButton(screen, "Speed: " + str(difficulty.getAutoFallSpeed()), (speedButtonLocationX, speedButtonLocationY), (60, 30),
                                    pygame.font.Font(None, 22), [themes.getBlue(), themes.getGray()])

    end_game_menu = EndGameMenu(board_manager)
    menu = TetrisStartMenu()
    menu.initialize()

    if menu.startGameFlag == True:
        gameActive = False

    while not gameActive:
        counter += 1
        if counter > interval:
            counter = 0

        # Check if we need to automatically go down
        if counter % (fps // difficulty.getAutoFallSpeed() // level) == 0 or pressing_down:
            if board_manager.get_game_state() == "start":
                board_manager.move_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = True
            if event.type == pygame.KEYDOWN:
                if event.key in event_key_action_list:
                    if event_key_action_list[event.key] == "true":
                        pressing_down = True
                    method_to_run = event_key_action_list[event.key]
                    if callable(method_to_run):
                        method_to_run()
            if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                pressing_down = False
            #Pause Button code
            if pauseIconButton.clickAction(event):
                main()
            # PUT ICON BUTTON clickAction here!
            # Dark mode Button Logic
            if darkModeButton.clickCheck(event):
                tetris_board.switch_board_color()
                darkModeButton.toggleDarkMode()
                if darkModeButton.getDarkModeToggle() == 1:
                    darkModeButton.changeText("Dark")
                elif darkModeButton.getDarkModeToggle() == 0:
                    darkModeButton.changeText("Light")
            # Theme Button logic
            if themeButton.clickCheck(event):
                newColor = themes.returnNextColor()
                tetris_block.set_colors(newColor)
                tetris_board.set_colors(newColor)
                themeButton.changeText(themes.findColorName(newColor))
            if speedButton.clickCheck(event):
                difficulty.increaseFallSpeed()

        tetris_board.draw_game_board(screen = screen)
        board_manager.draw_figure(screen = screen)
        board_checker.clear_lines()
        board_manager.draw_score(screen = screen)
        board_manager.draw_high_score(screen = screen)
        if board_manager.get_game_state() == "gameover":
            gameActive = True
            sound_manager.stop_background_music()
            sound_manager.play_game_over_sound()
        
    # PUT ICON BUTTONS HERE!
        # Pause Logic
        pauseIconButton.initialize()
        if pauseIconButton.keyAction(pygame.key.get_pressed()):
            main()
        # Add more button initializations
        darkModeButton.draw()
        themeButton.draw()
        speedButton.draw()
        speedButton.changeText("Speed: " + str(difficulty.getAutoFallSpeed()))

        # Refresh the screen
        pygame.display.flip()
        clock.tick(fps)

    board_manager.save_high_score()
    end_game_menu.initialize()


if __name__ == "__main__":
    main()