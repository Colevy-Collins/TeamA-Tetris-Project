import pygame
from src.TetrisButton import Button

class IconButton(Button):
    def __init__(self, screen, position, size, colors):
        super().__init__(screen, position, size, colors)

    def generate_icon(self):
        pass

    def draw(self, icon_rects):
        # Draw the button background
        pygame.draw.rect(self.screen, self.colors[1], (self.position[0], self.position[1], self.size, self.size), 100, 25)

        # Draw the pause icon (two vertical lines)
        for icon in icon_rects:
            pygame.draw.rect(self.screen, self.colors[1], icon, 40,)

