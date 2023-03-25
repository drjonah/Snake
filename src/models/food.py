import pygame, random

class Food():
    def __init__(self, surface, window_size, number_grid_lines, size_x, size_y) -> None:
        self.surface = surface
        self.window_size = window_size
        self.number_grid_lines = number_grid_lines
        self.size_x = size_x
        self.size_y = size_y

        self.pos_x = 0
        self.pos_y = 0

    def start_food(self) -> None:
        self.pos_x = random.randint(0, self.number_grid_lines - 1) * self.size_x
        self.pos_y = random.randint(0, self.number_grid_lines - 1) * self.size_y

    def spawn(self) -> None:
        rect = pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y)
        pygame.draw.rect(self.surface, (255, 255, 0), rect, 0)