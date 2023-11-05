from src.PygameDelegate import PygameDelegate
from src.TetrisBoard import TetrisBoard
from src.TetrisBlock import TetrisBlock
from src.TetrisBoardManager import BoardManager
from src.TetrisBoardChecker import BoardChecker
from src.SoundManager import SoundManager
from src.HighScoreHandler import HighScoreHandler
pygame = PygameDelegate()


def main():
    # Pygame init
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

    game_block_height = 20
    game_block_width = 10

    tetris_board.initialize_board(game_block_height, game_block_width) # code smell - what is 20 and 10? Can we use keyword argument? 
    
    starting_shift_x = 3 
    starting_shift_y = 0

    board_manager.create_figure(starting_shift_x, starting_shift_y)
    done = False
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

    while not done:
        counter += 1
        if counter > interval:
            counter = 0
            
        # Check if we need to automatically go down
        if counter % (fps // interval_of_auto_move // level) == 0 or pressing_down: 
            if board_manager.get_game_state() == "start":
                board_manager.move_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key in event_key_action_list:
                    if event_key_action_list[event.key] == "true":
                        pressing_down = True
                    method_to_run = event_key_action_list[event.key]
                    if callable(method_to_run):
                        method_to_run()
                        

            if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                pressing_down = False
                
        tetris_board.draw_game_board(screen = screen)
        
        # code smell - how many values duplication Figures[current_figure_type][current_rotation]
        board_manager.draw_figure(screen = screen)
        board_checker.clear_lines()
        if board_manager.get_game_state() == "gameover":
            sound_manager.stop_background_music()
            sound_manager.play_game_over_sound()
            done = True

        # refresh the screen
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()