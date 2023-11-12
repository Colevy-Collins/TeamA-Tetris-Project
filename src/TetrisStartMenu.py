import pygame
from src.TetrisDefaultUI import DefaultUI
from src.TetrisUIButton import TextButton


class TetrisStartMenu(DefaultUI):
    def __init__(self):
        super().__init__()

        self.start_button = TextButton(self.screen, "Start", (self.screen_width // 2, self.screen_height // 2 + 50), (100, 40), self.button_font, [self.WHITE, (0, 128, 255), self.BLACK, self.BLACK])

    def initialize(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.rect.collidepoint(event.pos):
                        # Handle button click (for example, start the game)
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
