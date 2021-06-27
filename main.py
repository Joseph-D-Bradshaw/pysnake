from snake import Snake
from utils import create_and_draw_grid, highlight_cell_at_x_y
from constants import CELL_SIZE, DARK_GREY, HEIGHT, WIDTH, CLOCK_CYCLE

import sys
import pygame

size = WIDTH, HEIGHT
X_CELLS_COUNT = WIDTH // CELL_SIZE
Y_CELLS_COUNT = HEIGHT // CELL_SIZE

if __name__ == '__main__':
    screen = pygame.display.set_mode(size)
    snake = Snake(screen, 1, 1)
    snake.add_part()
    snake.add_part()
    snake.add_part()
    snake.add_part()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(DARK_GREY)        
        grid_cells = create_and_draw_grid(screen)    
        snake.draw()
        pygame.display.flip()
