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