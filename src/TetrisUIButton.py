import pygame

class Button:
    def __init__(self, screen, text, position, size, font, colors):
        self.screen = screen
        self.text = text
        self.position = position
        self.size = size
        self.font = font
        self.colors = colors
        self.hovered = False

        # Create the button's rectangle
        self.rect = pygame.Rect(self.position[0] - self.size[0] // 2, self.position[1] - self.size[1] // 2, self.size[0], self.size[1])

    def draw(self):
        # Check if the mouse is hovering over the button
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

        # Create the button background and border
        button_color = self.colors[1] if self.hovered else self.colors[0]
        pygame.draw.rect(self.screen, self.colors[2], self.rect, 0)
        pygame.draw.rect(self.screen, self.colors[3], self.rect, 2)

        # Create the button text
        text_surface, text_rect = self.create_text_surface(self.text, self.font, button_color)
        text_rect.center = self.rect.center
        self.screen.blit(text_surface, text_rect)

    def create_text_surface(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()
