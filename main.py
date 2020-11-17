import pygame
from pygame.locals import *

from map_ import *
from node.node import Node
from solver import ARAStar_solver

SCREEN = pygame.display.set_mode(
    (map.GRID_X * map.GRID_SIZE + map.GRID_X * map.MARGIN + map.MARGIN,
     map.GRID_Y * map.GRID_SIZE + map.GRID_Y * map.MARGIN + map.MARGIN),
    pygame.RESIZABLE)

GRID_MAP = [[Node(x, y, "") for x in range(map.GRID_X)]
            for y in range(map.GRID_Y)]

START = GRID_MAP[map.GRID_X-1][0]
GOAL = GRID_MAP[0][map.GRID_Y-1]


def draw_path(path, color):
    for node in path:
        if node != START and node != GOAL:
            map.drawRect(color, node.x, node.y, SCREEN)
    map.drawRect(map.GREEN, START.x, START.y, SCREEN)


if __name__ == "__main__":
    pygame .init()
    pygame.display.flip()
    map.drawMap(GRID_MAP, START, GOAL, SCREEN)
    path = ARAStar_solver.ARAStarSolver(START, GOAL)
    if path:
        draw_path(path, map.BLUE)
    else:
        print("Unable to generate path from start to goal.")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
