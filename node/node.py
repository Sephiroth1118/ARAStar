import math


class Node:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.H = 0
        self.G = 0
        self.is_obstacle = False
        self.is_start = False
        self.is_goal = False
        self.parent = None
        self.children = []

    def getCost(self):
        if self.parent:
            cost = int(math.sqrt((self.x - self.parent.x)**2 +
                                 (self.y - self.parent.y)**2))
        else:
            cost = 0
        return cost

    def setObstacle(self):
        self.is_obstacle = True

    def isObstacle(self):
        return self.is_obstacle

    def setStart(self):
        self.is_start = True

    def isStart(self):
        return self.is_start

    def setGoal(self):
        self.is_goal = True

    def isGoal(self):
        return self.is_goal
