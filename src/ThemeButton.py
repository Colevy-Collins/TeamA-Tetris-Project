import pygame
from src.TetrisIconButton import IconButton
from src.Themes import Themes
from src.TetrisPauseMenu import PausedMenu
from src.TetrisButton import Button
themes = Themes()
class ThemeButton(Button):
    def __init__(self, screen, text, position, size, font, colors):
        super().__init__(screen, position, size, colors)
        self.text = text
        self.font = font

        # Create the button's rectangle
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.darkModeToggle = 0

    def draw(self):
        # Create the button background and border
        pygame.draw.rect(self.screen, super().currentColor()[1], self.rect, 0, border_radius=35)

        # Create the button text
        text_surface, text_rect = self.create_text_surface(self.text, self.font, super().currentColor()[0])
        text_rect.center = self.rect.center
        self.screen.blit(text_surface, text_rect)

    def create_text_surface(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def changeText(self, newText):
        print(newText)
        self.text = newText

    def getText(self):
        return self.text

    # def initialize(self):
    #     text_surface, text_rect = self.create_text_surface("Dark", pygame.font.Font(None, 37), themes.getGray())
    #
    #     self.screen.blit(text_surface, text_rect)
    #
    # def generate_icon(self):
    #     text_surface, text_rect = self.create_text_surface("Dark", pygame.font.Font(None, 37), themes.getGray())
    #
    #     self.screen.blit(text_surface, text_rect)
    #
    #     return 0
    #
    # def create_text_surface(self, text, font, color):
    #     text_surface = font.render(text, True, color)
    #     return text_surface, text_surface.get_rect()

    # def clickAction(self, events):
    #     if self.clickCheck(events):
    #         self.toggleDarkMode()
    #         print("Toggle: " + str(self.darkModeToggle))
    #         return self.darkModeToggle

    def keyAction(self, keys):
        pass

