import pygame

class Button:
    def __init__(self, screen, position, size, colors):
        self.screen = screen
        self.position = position
        self.size = size
        self.colors = colors
        

    def draw(self):
        pass

    def click_action(self):
        pass

    def hoverCheck(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_x, button_y, button_width, button_height = self.position[0], self.position[1], self.size[0], self.size[1]        
        if (button_x <= mouse_x <= button_x + button_width) and (button_y <= mouse_y <= button_y + button_height):
         
            return self.darken_color()
        else:
            return self.colors
    
    
    def darken_color(self, factor=0.6):
        darkColors = []
        for color in self.colors:
            r, g, b = color
            darkened_r = max(10, min(255, int(r * factor)))
            darkened_g = max(10, min(255, int(g * factor)))
            darkened_b = max(10, min(255, int(b * factor)))
            darkColors.append((darkened_r, darkened_g, darkened_b))
        return darkColors