import pygame, random

class Snake():
    def __init__(self, surface, window_size, number_grid_lines, size_x, size_y) -> None:
        self.surface = surface
        self.window_size = window_size
        self.number_grid_lines = number_grid_lines
        self.size_x = size_x
        self.size_y = size_y

        self.body = []

        self.speed_x = 0
        self.speed_y = 1

        self.pos_x = 0
        self.pos_y = 0

    def start_snake(self) -> None:
        self.pos_x = random.randint(5, self.number_grid_lines - 4) * self.size_x
        self.pos_y = random.randint(5, self.number_grid_lines - 4) * self.size_y

        self.body.append([self.pos_x, self.pos_y])

    def update_snake(self) -> None:
        self.body.insert(0,[self.pos_x, self.pos_y])
        del self.body[-1]

        for x, y in self.body:
            rect = pygame.Rect(x, y, self.size_x, self.size_y)
            pygame.draw.rect(self.surface, (255, 0, 0), rect, 0)

    def add_body(self) -> None:
        self.body.append([self.pos_x + (self.speed_x * self.size_x), self.pos_y + (self.speed_y * self.size_y)])

    def is_alive(self) -> bool:
        if self.body[0] in self.body[1:]:
            return False
        return True