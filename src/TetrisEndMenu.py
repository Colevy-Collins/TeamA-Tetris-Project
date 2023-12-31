import pygame
import sys
from src.TetrisUIButton import UIButton
from src.TetrisDefaultUI import DefaultUI

class EndGameMenu(DefaultUI):
    def __init__(self, board_manager):
        super().__init__()
        buttonWidth = 200
        self.board_manager = board_manager
        self.main_menu_button = UIButton(self.screen, "Main Menu", (self.screen_width // 2 - (buttonWidth / 2), self.screen_height // 2 + 50), (buttonWidth, 40), self.button_font, [self.WHITE, self.BLACK])
        self.quit_button = UIButton(self.screen, "Quit", (self.screen_width // 2 - (buttonWidth / 2), self.screen_height // 2 + 100), (buttonWidth, 40), self.button_font, [self.WHITE, self.BLACK])

    def initialize(self):
        self.running = True

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.buttonHandle(events)

            # Draw Score
            self.drawBackground()
            self.draw_score(self.screen)
            self.draw_high_score(self.screen)

            # Draw Buttons, Title and Background
            self.drawButton()
            self.drawTitle()

            # Update Screen
            pygame.display.flip()

    def drawBackground(self):
        # Set Background
        self.screen.fill(self.BLACK)

    def draw_score(self, screen):
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score: " + str(self.board_manager.get_score()), True, self.WHITE)
        screen.blit(text, [100, 200])

    def draw_high_score(self, screen):
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("High Score: " + str(self.board_manager.get_high_score()), True, self.WHITE)
        screen.blit(text, [100, 230])


    def drawButton(self):
        # Draw buttons
        self.main_menu_button.draw()
        self.quit_button.draw()

    def drawTitle(self):         
        # Initialize the title
        self.title_text = "Game Over"
        self.title_x, self.title_y = 100, 100
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

        if self.quit_button.clickCheck(events):
            self.running = False
            pygame.quit()
            sys.exit()