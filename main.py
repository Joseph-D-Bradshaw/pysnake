import threading
from snake import Heading, Snake
from utils import create_and_draw_grid
from constants import CELL_SIZE, CLOCK_CYCLE, DARK_GREY, EAT_EVENT, HEIGHT, MOVE_EVENT, WIDTH

import sys
import pygame

SIZE = WIDTH, HEIGHT
X_CELLS_COUNT = WIDTH // CELL_SIZE
Y_CELLS_COUNT = HEIGHT // CELL_SIZE

if __name__ == '__main__':
    clock = pygame.time.Clock().tick(60)
    screen = pygame.display.set_mode(SIZE)
    snake = Snake(screen, 1, 1)
    
    pygame.init()
    pygame.time.set_timer(MOVE_EVENT, CLOCK_CYCLE)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    pygame.event.post(pygame.event.Event(EAT_EVENT))
                elif key[pygame.K_UP]:
                    snake.heading = Heading.NORTH
                elif key[pygame.K_DOWN]:
                    snake.heading = Heading.SOUTH
                elif key[pygame.K_LEFT]:
                    snake.heading = Heading.WEST
                elif key[pygame.K_RIGHT]:
                    snake.heading = Heading.EAST
            elif event.type == MOVE_EVENT:
                snake.move()
            elif event.type == EAT_EVENT:
                snake.add_part()
        screen.fill(DARK_GREY)
        grid_cells = create_and_draw_grid(screen)    
        snake.draw()
        pygame.display.flip()
