import pygame
import random

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


def drawMap(grid, start, goal, screen, percent_chance_for_obstacle=10):
    for x in range(GRID_X):
        for y in range(GRID_Y):
            if grid[x][y] != start and grid[x][y] != goal:
                if random.randint(1, 100) <= percent_chance_for_obstacle:
                    grid[x][y].setObstacle()
            if getNorthGrid(grid, x, y, GRID_Y):
                grid[x][y].children.append(getNorthGrid(grid, x, y, GRID_Y))
            if getSouthGrid(grid, x, y, GRID_Y):
                grid[x][y].children.append(getSouthGrid(grid, x, y, GRID_Y))
            if getWestGrid(grid, x, y, GRID_X):
                grid[x][y].children.append(getWestGrid(grid, x, y, GRID_X))
            if getEastGrid(grid, x, y, GRID_X):
                grid[x][y].children.append(getEastGrid(grid, x, y, GRID_X))
            if getNorthWestGrid(grid, x, y, GRID_X, GRID_Y):
                grid[x][y].children.append(
                    getNorthWestGrid(grid, x, y, GRID_X, GRID_Y))
            if getNorthEastGrid(grid, x, y, GRID_X, GRID_Y):
                grid[x][y].children.append(
                    getNorthEastGrid(grid, x, y, GRID_X, GRID_Y))
            if getSouthWestGrid(grid, x, y, GRID_X, GRID_Y):
                grid[x][y].children.append(
                    getSouthWestGrid(grid, x, y, GRID_X, GRID_Y))
            if getSouthEastGrid(grid, x, y, GRID_X, GRID_Y):
                grid[x][y].children.append(
                    getSouthEastGrid(grid, x, y, GRID_X, GRID_Y))
    for x in range(GRID_X):
        for y in range(GRID_Y):
            if x == start.x and y == start.y:
                drawRect(GREEN, x, y, screen)
            elif x == goal.x and y == goal.y:
                drawRect(RED, x, y, screen)
            elif grid[x][y].isObstacle:
                drawRect(BLACK, x, y, screen)
            else:
                drawRect(WHITE, x, y, screen)


def getNorthGrid(grid, x, y, GRID_Y):
    if y < GRID_Y - 1 and not grid[x][y+1].isObstacle:
        return grid[x][y+1]


def getSouthGrid(grid, x, y, GRID_Y):
    if y > 0 and not grid[x][y-1].isObstacle:
        return grid[x][y-1]


def getWestGrid(grid, x, y, GRID_X):
    if x > 0 and not grid[x-1][y].isObstacle:
        return grid[x-1][y]


def getEastGrid(grid, x, y, GRID_X):
    if x < GRID_X - 1 and not grid[x+1][y].isObstacle:
        return grid[x+1][y]


def getNorthWestGrid(grid, x, y, GRID_X, GRID_Y):
    if x > 0 and y < GRID_Y - 1 and not grid[x-1][y+1].isObstacle:
        return grid[x-1][y+1]


def getNorthEastGrid(grid, x, y, GRID_X, GRID_Y):
    if x < GRID_X - 1 and y < GRID_Y - 1 and not grid[x+1][y+1].isObstacle:
        return grid[x+1][y+1]


def getSouthWestGrid(grid, x, y, GRID_X, GRID_Y):
    if x > 0 and y > 0 and not grid[x-1][y-1].isObstacle:
        return grid[x-1][y-1]


def getSouthEastGrid(grid, x, y, GRID_X, GRID_Y):
    if x < GRID_X - 1 and y > 0 and not grid[x+1][y-1].isObstacle:
        return grid[x+1][y-1]
