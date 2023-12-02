import pygame
import sys
from src.TetrisDefaultUI import DefaultUI
from src.TetrisUIButton import UIButton

class TetrisStartMenu(DefaultUI):
    def __init__(self):
        super().__init__()

        buttonWidth = 100
        self.startGameFlag = False

        self.start_button = UIButton(self.screen, "Start", (self.screen_width // 2 - (buttonWidth // 2) , self.screen_height // 2 + 50), (buttonWidth, 40), self.button_font, [self.WHITE, self.GREY])
        self.quit_button = UIButton(self.screen, "Quit", (self.screen_width // 2 - (buttonWidth // 2) , self.screen_height // 2 + 115), (buttonWidth, 40), self.button_font, [self.WHITE, self.GREY])


    def initialize(self):
        self.running = True
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.buttonHandle(events)

                
            # Draw Buttons Title and Background
            self.drawBackground()
            self.drawButton()
            self.drawTitle()

            # Update Screen
            pygame.display.flip()

    def drawBackground(self):
            # Draw the Tetris background
            self.background = pygame.image.load('src/background.png')
            self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
            self.screen.blit(self.background, (0, 0))

    def drawButton(self):
        # Draw buttons
        self.start_button.draw()
        self.quit_button.draw()

    def drawTitle(self):
        self.title_text = "TETRIS"
        self.title_colors = [self.RED, self.GREEN, self.BLUE, self.RED, self.GREEN, self.BLUE]  # Example colors for each letter
        self.title_x, self.title_y = 100, 100
    
        # Create a background for the title
        title_rect = pygame.Rect(self.title_x - 15, self.title_y - 10, 240, 50)
        pygame.draw.rect(self.screen, self.BLACK, title_rect)
            
        # Create title text with different colors for each letter
        for i, letter in enumerate(self.title_text):
            letter_surface, letter_rect = self.create_text_surface(letter, self.title_font, self.title_colors[i])
            letter_rect.topleft = (self.title_x + i * 36, self.title_y)
            self.screen.blit(letter_surface, letter_rect)
    
    def buttonHandle(self, events):         
        if self.start_button.clickCheck(events):
            self.startGameFlag = True
            self.running = False

        if self.quit_button.clickCheck(events):
            self.running = False
            pygame.quit()
            sys.exit()