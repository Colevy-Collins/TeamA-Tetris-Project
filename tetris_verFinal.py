from src.PygameDelegate import PygameDelegate
from src.TetrisBoard import TetrisBoard
from src.TetrisBlock import TetrisBlock
from src.TetrisBoardManager import BoardManager
from src.TetrisBoardChecker import BoardChecker
from src.TetrisStartMenu import TetrisStartMenu
from src.TetrisEndMenu import EndGameMenu
from src.TetrisPauseMenu import PausedMenu
from src.TetrisPauseIcon import PauseIconButton


pygame = PygameDelegate()

def main():   

    tetris_block = TetrisBlock()
    tetris_board = TetrisBoard()
    board_manager = BoardManager(tetris_block, tetris_board)
    board_checker = BoardChecker(tetris_board)
 
    # Pygame related init
    pygame.init()
    screen = pygame.display.set_mode(board_manager.get_window_size())
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

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
    interval_of_auto_move = 2

    event_key_action_list = {
        pygame.K_UP: lambda: board_manager.rotate_figure(),
        pygame.K_DOWN: "true",
        pygame.K_LEFT: lambda: board_manager.move_sideways(-1),
        pygame.K_RIGHT: lambda: board_manager.move_sideways(1),
        pygame.K_SPACE: lambda: board_manager.move_to_bottom()
    }

    pausebuttonSize = 40
    pausebuttonLocationX = 10
    pausebuttonLocationY = 10

    pauseIconButton = PauseIconButton(screen, (pausebuttonLocationX, pausebuttonLocationY), pausebuttonSize, [(0, 0, 0 ), (255, 0, 0)])
    end_game_menu = EndGameMenu()
    menu = TetrisStartMenu()
    menu.initialize()

    if menu.startGameFlag == True:
        #Below variable when changed to false runs game logic
        gameActive = False

    while not gameActive:

        keys = pygame.key.get_pressed()
        #BELOW If P is pressed, Pause menu 
        if keys[pygame.K_p]:
            paused_menu = PausedMenu()
            paused_menu.initialize()

            if paused_menu.menuAction == True:
                main()
            if paused_menu.resumeAction == True:
                clock.tick(fps)

        counter += 1
        if counter > interval:
            counter = 0

        # Check if we need to automatically go down
        if counter % (fps // interval_of_auto_move // level) == 0 or pressing_down: 
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
           # if event.type == pygame.MOUSEBUTTONDOWN:
               # if event.button == 1:  # Check for left mouse button click
                 #   mouse_x, mouse_y = pygame.mouse.get_pos()
                    #if (pausebuttonLocationX <= mouse_x <= pausebuttonLocationX + pausebuttonSize) and (pausebuttonLocationY <= mouse_y <= pausebuttonLocationY + pausebuttonSize):
                        # Pause button was clicked, handle the pause action
                        #paused_menu = PauseIconButton()
                        #paused_menu.initialize()

                        #if paused_menu.menuAction == True:
                        #    main()
                        #if paused_menu.resumeAction == True:
                       #     clock.tick(fps)
                    
        tetris_board.draw_game_board(screen = screen)
            
        # code smell - how many values duplication Figures[current_figure_type][current_rotation]
        board_manager.draw_figure(screen = screen)
        board_checker.clear_lines()
        if board_manager.get_game_state() == "gameover":
            gameActive = True

        # refresh the screen
        pauseIconButton.initialize()

        pygame.display.flip()
        clock.tick(fps)

    end_game_menu.initialize()
    main()


if __name__ == "__main__":
    main()