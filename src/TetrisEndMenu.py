import pygame
import sys
from src.TetrisUIButton import Button
from src.TetrisDefaultUI import DefaultUI

class EndGameMenu(DefaultUI):
    def __init__(self):
        super().__init__()
        
        self.screen.fill(self.BLACK)

        # Fonts
        self.title_font = pygame.font.Font(None, 50)
        self.button_font = pygame.font.Font(None, 37)

        # Initialize the menu components
        self.title_text = "Game Over"
        self.title_x, self.title_y = 100, 100

        self.quit_button = Button(self.screen, "Quit", (self.screen_width // 2, self.screen_height // 2 + 50), (100, 40), self.button_font, [self.WHITE, (255, 0, 0), self.BLACK, self.BLACK])
        self.main_menu_button = Button(self.screen, "Main Menu", (self.screen_width // 2, self.screen_height // 2 + 100), (100, 40), self.button_font, [self.WHITE, (0, 128, 255), self.BLACK, self.BLACK])

    def initialize(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.quit_button.rect.collidepoint(event.pos):
                        # Handle quit button click
                        pygame.quit()
                        sys.exit()
                    elif self.main_menu_button.rect.collidepoint(event.pos):
                        # Handle main menu button click (return to the main menu)
                        self.running = False

            
            
            self.screen.fill(self.BLACK)


            # Create a background for the title
            title_rect = pygame.Rect(self.title_x - 15, self.title_y - 10, 240, 50)
            pygame.draw.rect(self.screen, self.BLACK, title_rect)

            # Create title text
            title_surface, title_rect = self.create_text_surface(self.title_text, self.title_font, self.WHITE)
            title_rect.topleft = (self.title_x, self.title_y)
            self.screen.blit(title_surface, title_rect)

            # Draw the buttons
            self.quit_button.draw()
            self.main_menu_button.draw()

            pygame.display.flip()
