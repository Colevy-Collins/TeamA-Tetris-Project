import pygame
from src.TetrisDefaultUI import DefaultUI
from src.TetrisUIButton import UIButton


class TetrisStartMenu(DefaultUI):
    def __init__(self):
        super().__init__()
        self.start_button = UIButton(self.screen, "Start", (self.screen_width // 2, self.screen_height // 2 + 50), (100, 40), self.button_font, [self.WHITE, self.GREY])

    def initialize(self):
        while self.running:
            self.start_button.hoverCheck()
            if self.start_button.click_action():
                self.startGameFlag = True
                self.running = False

            # Draw the Tetris background
            self.screen.blit(self.background, (0, 0))

            # Create a background for the title
            title_rect = pygame.Rect(self.title_x - 15, self.title_y - 10, 240, 50)
            pygame.draw.rect(self.screen, self.BLACK, title_rect)
            
            # Create title text with different colors for each letter
            for i, letter in enumerate(self.title_text):
                letter_surface, letter_rect = self.create_text_surface(letter, self.title_font, self.title_colors[i])
                letter_rect.topleft = (self.title_x + i * 36, self.title_y)
                self.screen.blit(letter_surface, letter_rect)

            # Draw the "Start" button
            self.start_button.draw()

            pygame.display.flip()
