import pygame, sys, time
from models import Board, Snake, Food # objects
  
SIZE = (500, 500)
GRID_LINES = 20

CUBE_SIZE_X = SIZE[0] // GRID_LINES
CUBE_SIZE_Y = SIZE[1] // GRID_LINES

pygame.init()

surface = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snake ... by Your Mom")

clock = pygame.time.Clock()
clock_speed = 9

board = Board(surface, SIZE, GRID_LINES, CUBE_SIZE_X, CUBE_SIZE_Y)
board.create_grid()

snake = Snake(surface, SIZE, GRID_LINES, CUBE_SIZE_X, CUBE_SIZE_Y)
snake.start_snake()

food = Food(surface, SIZE, GRID_LINES, CUBE_SIZE_X, CUBE_SIZE_Y)
food.start_food() 

### GAME RUN ##
game_run = True  
while game_run:
    # draw board
    board.reset_surface()
    board.draw_score()
    board.draw_grid()

    # logic
    if not snake.is_alive():
        break

    if food.pos_x == snake.pos_x and food.pos_y == snake.pos_y:
        board.score += 1
        if board.score % 5 == 0:
            clock_speed += 1

        snake.add_body()
        food.start_food()
    
    # spawn food
    food.spawn()

    # update snake
    snake.update_snake()
    snake.pos_x += snake.speed_x * CUBE_SIZE_X
    snake.pos_x %= SIZE[0]
    snake.pos_y += snake.speed_y * CUBE_SIZE_Y
    snake.pos_y %= SIZE[1]
    # update
    pygame.display.flip()
    clock.tick(clock_speed)

    # keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.speed_y = -1
                snake.speed_x = 0
            if event.key == pygame.K_DOWN:
                snake.speed_y = 1
                snake.speed_x = 0
            if event.key == pygame.K_LEFT:
                snake.speed_y = 0
                snake.speed_x = -1
            if event.key == pygame.K_RIGHT:
                snake.speed_y = 0
                snake.speed_x = 1

### GAME OVER ###
board.end()
snake.update_snake()
time.sleep(2)

pygame.quit()
sys.exit()