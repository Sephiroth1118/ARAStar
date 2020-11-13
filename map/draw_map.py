import pygame

MARGIN = 2
[GRID_SIZE, GRID_X, GRID_Y] = [10, 50, 50]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 204, 204)


def drawRect(color, x, y, screen):
    pygame.draw.rect(screen, color,
                     [(MARGIN + GRID_SIZE) * x + MARGIN,
                      (MARGIN + GRID_SIZE) * y + MARGIN,
                      GRID_SIZE, GRID_SIZE])
