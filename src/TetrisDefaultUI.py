import pygame
#from src.TetrisUIButton import TextButton
 
class DefaultUI:
    def __init__(self):
        pygame.init()

        # Constants for colors
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)
        self.GREY = (100,100,100)

        # Screen dimensions
        self.screen_width, self.screen_height = 400, 500

        # Create the screen
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Tetris")

        # Fonts
        self.title_font = pygame.font.Font(None, 50)
        self.button_font = pygame.font.Font(None, 37)


    def create_text_surface(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()
    
    def initialize(self):
        pass

    def draw(self):
        pass

    def drawButton(self):
        pass

    def drawTitle(self):
        pass

    def buttonHandle(self):
        pass