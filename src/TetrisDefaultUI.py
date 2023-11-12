import pygame
from src.TetrisUIButton import TextButton
 

class DefaultUI:
    def __init__(self):
        pygame.init()

        # Constants for colors
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)

        self.startGameFlag = False

        # Screen dimensions
        self.screen_width, self.screen_height = 400, 500

        # Create the screen
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Tetris")

        # Background image (replace 'background.jpg' with your Tetris background image)
        self.background = pygame.image.load('src/background.png')
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))

        # Fonts
        self.title_font = pygame.font.Font(None, 50)
        self.button_font = pygame.font.Font(None, 37)

        self.title_text = "TETRIS"
        self.title_colors = [self.RED, self.GREEN, self.BLUE, self.RED, self.GREEN, self.BLUE]  # Example colors for each letter
        self.title_x, self.title_y = 100, 100

        self.start_button = TextButton(self.screen, "Start", (self.screen_width // 2, self.screen_height // 2 + 50), (100, 40), self.button_font, [self.WHITE, (0, 128, 255), self.BLACK, self.BLACK])

        self.running = True

    def create_text_surface(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()