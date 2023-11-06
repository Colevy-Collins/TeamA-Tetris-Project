import pygame

class PauseButton:
    def __init__(self, screen, position, size, icon_color, background_color):
        self.screen = screen
        self.position = position
        self.size = size
        self.normal_icon_color = icon_color
        self.hover_icon_color = (191, 191, 191)
        self.normal_rect_color = background_color
        self.hover_rect_color = (75, 75, 75)
        self.icon_rects = []

        self.generate_icon()

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

    def draw(self):
    # Check if the mouse is hovering over the button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        is_hovered = (self.position[0] <= mouse_x <= self.position[0] + self.size) and (self.position[1] <= mouse_y <= self.position[1] + self.size)

        # Use the appropriate colors based on hover state
        rect_color = self.hover_rect_color if is_hovered else self.normal_rect_color
        icon_color = self.hover_icon_color if is_hovered else self.normal_icon_color

        # Draw the button background
        pygame.draw.rect(self.screen, rect_color, (self.position[0], self.position[1], self.size, self.size), 100, 25)

        # Draw the pause icon (two vertical lines)
        for icon_rect in self.icon_rects:
            pygame.draw.rect(self.screen, icon_color, icon_rect)

