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
    sizeValues = [40, 40, 40] # button sizeX, button sizeY, Icon Size
    pausebuttonLocationX = 10
    pausebuttonLocationY = 10
    
    pauseIconButton = PauseIconButton(screen, (pausebuttonLocationX, pausebuttonLocationY), sizeValues, [(150, 150, 150 ), (255, 255, 255)])
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