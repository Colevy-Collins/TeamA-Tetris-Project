import pygame
import sys
from src.TetrisUIButton import UIButton
from src.TetrisDefaultUI import DefaultUI

class PausedMenu(DefaultUI):
    def __init__(self):
        super().__init__()
        buttonWidth = 100
        self.title_x, self.title_y = 100, 100

        self.resume_button = UIButton(self.screen, "Resume", (self.screen_width // 2 - (buttonWidth // 2), self.screen_height // 2), (buttonWidth, 40), self.button_font, [self.WHITE, self.BLACK])
        self.main_menu_button = UIButton(self.screen, "Main Menu", (self.screen_width // 2 - (buttonWidth // 2), self.screen_height // 2 + 50), (buttonWidth, 40), self.button_font, [self.WHITE, self.BLACK])


    def initialize(self):
        self.running = True
        self.menuAction = False

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
        # Set Background
        self.screen.fill(self.BLACK)

    def drawButton(self):
        # Draw buttons
        self.resume_button.draw()
        self.main_menu_button.draw()


    def drawTitle(self):         
        # Initialize the title
        self.title_text = "Paused"
        self.title_x, self.title_y = 135, 100
        self.title_colors = [self.WHITE]  
    
        # Create a background for the title
        title_rect = pygame.Rect(self.title_x - 15, self.title_y - 10, 240, 50)
        pygame.draw.rect(self.screen, self.BLACK, title_rect)
            
        # Create title text with different colors for each letter
        title_surface, title_rect = self.create_text_surface(self.title_text, self.title_font, self.WHITE)
        title_rect.topleft = (self.title_x, self.title_y)
        self.screen.blit(title_surface, title_rect)
    
    def buttonHandle(self, events):         
        if self.main_menu_button.clickCheck(events):
            self.running = False
            self.menuAction = True

        if self.resume_button.clickCheck(events):
            self.running = False
            
   