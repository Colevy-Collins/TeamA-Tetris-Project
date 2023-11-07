import pygame
from src.TetrisButton import Button

class UIButton(Button):
    def __init__(self, screen, text, position, size, font, colors):
        super().__init__(screen, position, size, colors)
        self.text = text
        self.font = font

        # Create the button's rectangle
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def draw(self):
        # Create the button background and border
        pygame.draw.rect(self.screen, super().hoverCheck()[1], self.rect, 0)

        # Create the button text
        text_surface, text_rect = self.create_text_surface(self.text, self.font, super().hoverCheck()[0])
        text_rect.center = self.rect.center
        self.screen.blit(text_surface, text_rect)

    def create_text_surface(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()
    
    def click_action(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos):
                        return True
                    

