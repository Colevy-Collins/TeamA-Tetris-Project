import pygame
from src.TetrisUIButton import UIButton
from src.TetrisDefaultUI import DefaultUI

class PausedMenu(DefaultUI):
    def __init__(self):
        super().__init__()  # Calls the constructor of the DefaultUI class

        # Semi-transparent black background with 50% opacity
        self.background = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        pygame.draw.rect(self.background, (0, 0, 0, 128), (0, 0, self.screen_width, self.screen_height))

        # Initialize the menu components
        self.menuAction = False
        self.resumeAction = False

        self.title_text = "Paused"
        self.title_x = (self.screen_width - self.title_font.size(self.title_text)[0]) // 2

        self.title_y = 100

        self.resume_button = UIButton(self.screen, "Resume", (self.screen_width // 2, self.screen_height // 2 + 50), (100, 40), self.button_font, [self.WHITE, self.BLACK])
        self.main_menu_button = UIButton(self.screen, "Main Menu", (self.screen_width // 2, self.screen_height // 2 + 100), (100, 40), self.button_font, [self.WHITE, self.BLACK])

    def initialize(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.resume_button.rect.collidepoint(event.pos):
                        # Handle resume button click
                        self.running = False
                        self.resumeAction = True
                    elif self.main_menu_button.rect.collidepoint(event.pos):
                        # Handle main menu button click (return to the main menu)
                        self.running = False
                        self.menuAction = True

            # Draw the semi-transparent black background
            self.screen.blit(self.background, (0, 0))

            # Create title text
            title_surface, title_rect = self.create_text_surface(self.title_text, self.title_font, self.WHITE)
            title_rect.topleft = (self.title_x, self.title_y)
            self.screen.blit(title_surface, title_rect)

            # Draw the buttons
            self.resume_button.draw()
            self.main_menu_button.draw()

            pygame.display.flip()