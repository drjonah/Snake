import pygame

class Board:
    def __init__(self, surface, window_size, number_grid_lines, size_x, size_y) -> None:
        # board attributes
        self.surface = surface
        self.window_size = window_size
        self.number_grid_lines = number_grid_lines
        self.size_x = size_x
        self.size_y = size_y

        self.score_font = pygame.font.Font(None, 350)
        self.end_font = pygame.font.Font(None, 50)

        self.grid_points = list()

        self.score = 0

    def create_grid(self) -> None:
        for x in range(self.number_grid_lines):
            for y in range(self.number_grid_lines):
                self.grid_points.append([x * self.size_x, y * self.size_y])

    def draw_grid(self) -> None:
        for x, y in self.grid_points:
            rect = pygame.Rect(x, y, self.size_x, self.size_y)
            pygame.draw.rect(self.surface, (255, 255, 255), rect, 1)

    def reset_surface(self) -> None:
        self.surface.fill((0,0,0))

    def draw(self, font, text: str) -> None:
        score_text = font.render(text, False, (0, 0, 255))
        text_rect = score_text.get_rect(center=(self.window_size[0]/2, self.window_size[1]/2))
        self.surface.blit(score_text, text_rect)

    def draw_score(self) -> None:
        self.draw(self.score_font, str(self.score))

    def end(self) -> None:
        self.reset_surface()
        self.draw(self.end_font, f'GAME OVER ... SCORE: {self.score}')
        pygame.display.flip()