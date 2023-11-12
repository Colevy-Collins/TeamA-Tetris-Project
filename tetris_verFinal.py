from src.PygameDelegate import PygameDelegate
from src.Button import Button
from src.TetrisBoard import TetrisBoard
from src.TetrisBlock import TetrisBlock
from src.TetrisBoardManager import BoardManager
from src.TetrisBoardChecker import BoardChecker
from src.TetrisStartMenu import TetrisStartMenu
from src.TetrisEndMenu import EndGameMenu
from src.TetrisPauseMenu import PausedMenu
from src.TetrisPauseIcon import PauseButton
from src.Difficulty import Difficulty
#from src.TetrisUIButton import TextButton
from src.Themes import Themes
from src.SoundManager import SoundManager
from src.HighScoreHandler import HighScoreHandler

from src.TetrisPauseIcon import PauseIconButton

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
    high_score_handler = HighScoreHandler('data', 'high_score.txt')
    board_manager = BoardManager(tetris_block, tetris_board, sound_manager, high_score_handler)
    board_checker = BoardChecker(tetris_board, sound_manager)

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
    pausebuttonSize = 40
    pausebuttonLocationX = 10
    pausebuttonLocationY = 10
    darkModeButtonLocationX = 47
    darkModeButtonLocationY = 100
    themeButtonLocationX = 47
    themeButtonLocationY = 160
    speedButtonLocationX = 350
    speedButtonLocationY = 20
    #Button Creation
    pauseIconButton = PauseButton(screen, (pausebuttonLocationX, pausebuttonLocationY), pausebuttonSize, (255, 255, 255), (0, 0, 0))
    darkModeButton = TextButton(screen, "Dark", (darkModeButtonLocationX, darkModeButtonLocationY), (80, 30), pygame.font.Font(None, 18), [WHITE, (0, 128, 255), themes.getGray(), themes.getGray()])
    themeButton = TextButton(screen, "Theme", (themeButtonLocationX, themeButtonLocationY), (80, 30), pygame.font.Font(None, 20), [WHITE, (0, 128, 255), themes.getGray(), themes.getGray()])


    sizeValues = [40, 40, 40] # button sizeX, button sizeY, Icon Size
    pausebuttonLocationX = 10
    pausebuttonLocationY = 10
    
    pauseIconButton = PauseIconButton(screen, (pausebuttonLocationX, pausebuttonLocationY), sizeValues, [(150, 150, 150 ), (255, 255, 255)])
    darkModeButton = 
    end_game_menu = EndGameMenu()
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
            # . . .

            
        tetris_board.draw_game_board(screen = screen)
        board_manager.draw_figure(screen = screen)
        board_checker.clear_lines()
        if board_manager.get_game_state() == "gameover":
            gameActive = True
            sound_manager.stop_background_music()
            sound_manager.play_game_over_sound()
            done = True
        
    # PUT ICON BUTTONS HERE!
        # Pause Logic
        pauseIconButton.initialize()
        if pauseIconButton.keyAction(pygame.key.get_pressed()):
            main()
        # Add more button logic here
        # . . .

        # Refresh the screen
        pygame.display.flip()
        clock.tick(fps)

    end_game_menu.initialize()
    main()


if __name__ == "__main__":
    main()