from src.RandomDelegate import RandomDelegate
random = RandomDelegate()

class TetrisBlock:
    def __init__(self):
        self.current_figure_type = 0
        self.current_figure_color = 0
        self.current_rotation = 0
        self.shift_in_x = 0
        self.shift_in_y = 0
        self.colors = (
            (0, 0, 0), # can not use index 0
            (120, 37, 179), 
            (100, 179, 179),
            (80, 34, 22),
            (80, 134, 22),
            (180, 34, 22),
            (180, 34, 122),
        )
        self.Figures = (
            [(1, 5, 9, 13), (4, 5, 6, 7)],
            [(4, 5, 9, 10), (2, 6, 5, 9)],
            [(6, 7, 9, 10), (1, 5, 6, 10)],
            [(1, 2, 5, 9), (0, 4, 5, 6), (1, 5, 9, 8), (4, 5, 6, 10)],
            [(1, 2, 6, 10), (5, 6, 7, 9), (2, 6, 10, 11), (3, 5, 6, 7)],
            [(1, 4, 5, 6), (1, 4, 5, 9), (4, 5, 6, 9), (1, 5, 6, 9)],
            [(1, 2, 5, 6)],
        )

    def create_figure(self, starting_shift_x, starting_shift_y):
        start_of_range = 0
        self.shift_in_x = starting_shift_x
        self.shift_in_y = starting_shift_y
        self.current_figure_type = random.randint(start_of_range, len(self.Figures) - 1)
        start_of_range = 1
        self.current_figure_color =random.randint(start_of_range, len(self.colors) - 1) 
        default_rotation = 0
        rotation_identifier = default_rotation
        self.current_rotation = rotation_identifier 

    def get_current_figure_type(self):
        return self.current_figure_type

    def get_current_figure_color(self):
        return self.current_figure_color

    def set_current_rotation(self, value):
        self.current_rotation = value
    
    def get_current_rotation(self):
        return self.current_rotation
    
    def get_shape(self):
        return self.Figures[self.current_figure_type][self.current_rotation]
    
    def get_figure(self):
        return self.Figures
    
    def get_shift_in_x(self):
        return self.shift_in_x

    def set_shift_in_x(self, value):
        self.shift_in_x = value

    def get_shift_in_y(self):
        return self.shift_in_y

    def set_shift_in_y(self, value):
        self.shift_in_y = value

    # Getter and setter for colors
    def get_colors(self):
        return self.colors

    def set_colors(self, value):
        self.colors = value

    # Method to append to colors
    def append_to_colors(self, value):
        self.colors.append(value)

    def set_current_figure_type(self, value):
        self.current_figure_type = value
    