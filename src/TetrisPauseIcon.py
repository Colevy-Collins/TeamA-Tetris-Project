import pygame
from src.TetrisIconButton import IconButton

class PauseIconButton(IconButton):
    def __init__(self, screen, position, size, colors):
        super().__init__(screen, position, size, colors)
        
        self.icon_rects = []
        self.generate_icon()


    def initialize(self):
        self.draw(self.icon_rects)

    def generate_icon(self):
        # Define the geometry of the pause icon
        icon_width = self.size // 10
        icon_height = self.size // 2
        icon_padding = self.size // 3

        # Calculate the coordinates of the two vertical lines
        line1_x = self.position[0] + icon_padding
        line2_x = self.position[0] + self.size - icon_width - icon_padding
        line_y = self.position[1] + icon_padding - 3

        # Create the two vertical lines (rectangles)
        line1 = pygame.Rect(line1_x, line_y, icon_width, icon_height)
        line2 = pygame.Rect(line2_x, line_y, icon_width, icon_height)

        self.icon_rects = [line1, line2]

    def click_action(self):
        pass

    
