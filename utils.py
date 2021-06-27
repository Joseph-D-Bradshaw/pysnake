import pygame
import threading
import time
from typing import Callable, List

from constants import CELL_SIZE, GREEN, HEIGHT, WIDTH, LIGHT_GREY

def create_and_draw_grid(surface) -> List[pygame.Rect]:
    grid_coords = []
    for x in range(WIDTH // 20):
        for y in range(HEIGHT // 20):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, LIGHT_GREY, rect, 1)
            grid_coords.append(rect)
    return grid_coords

def highlight_cell_at_x_y(surface, x: int, y: int):
    pygame.draw.rect(surface, GREEN, pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
