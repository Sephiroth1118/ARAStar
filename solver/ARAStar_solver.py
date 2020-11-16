import time
from node import *


def getEstimateDistance(current, goal):
    if current == goal:
        return 0
    else:
        # Manhattan distance.
        return abs(current.x-goal.x) + abs(current.y-goal.y)


def getImprovedSolution(goal, open_list, epsilon, path_cost):
    closed_list = set()
    while open_list:
        current_node = min(open_list, key=lambda o: o.G + epsilon * o.H)
        # 如果经过这个点的路径的cost大于已有的最佳路径，返回None。
        if current_node.G + epsilon * current_node.H > path_cost:
            return None

        open_list.remove(current_node)
        closed_list.add(current_node)
        for node in current_node.children:
            if node.isObstacle:
                continue
            if node in open_list or node in closed_list:
                if node.G < current_node.G + node.cost:
                    continue
            if current_node.parent:
                current_node.G = current_node.parent.G + current_node.cost()
            if node.G + node.H > path_cost:
                continue

            if node in open_list:
                new_G = current_node.G + node.cost()
                if node.G > new_G:
                    node.G = new_G
                    node.parent = current_node
            else:
                node.parent = current_node
                node.G = current_node.G + node.cost()
                if node != goal:
                    node.H = getEstimateDistance(node, goal)
                else:
                    node.H = 1
                    path = []
                    while node.parent:
                        path.append(node)
                        node = node.parent
                    path.append(node)
                    return path[::-1]
                open_list.add(node)
    return None


def ARAStar_solver(start, goal):
    open_list = set()
    closed_list = set()
    current_path = []
    path_cost = 1e9
    current_node = start
    current_node.H = getEstimateDistance(current_node, goal)
    open_list.add(current_node)
    temp = max(open_list, key=lambda o: (path_cost - o.G) / o.H)
    epsilon = 4e4
    epsilon_delta = epsilon / 10.0

    # 当open_list中依然有node的时候。
    while open_list:
        temp_list = open_list
        new_solution = getImprovedSolution(goal, temp_list, epsilon, path_cost)
        if new_solution:
            path_cost = new_solution[-1].G
            current_path = new_solution
            time.sleep(0.5)
        else:
            return current_path
        epsilon -= epsilon_delta
    return current_path


def solver(start, goal):
    openList = set()
    closedList = set()
    incumbent = []
    # s
    current = start

    # sets the start nodes heuristic
    current.H = ED(current, goal)

    # adds start to open list
    openList.add(current)

    # G
    pathCost = 10000000000

    # w0
    temp = max(openList, key=lambda o: (pathCost - o.G) / o.H)
    weight = 300000
    weightDelta = weight / 10

    # while there are nodes in the open list
    while openList:
        tempList = openList
        NewSolution = improved_solution(goal, tempList, weight, pathCost)

        if NewSolution:
            pathCost = NewSolution[-1].G
            incumbent = NewSolution
            drawPath(incumbent, randomColor())
            time.sleep(.5)
        else:
            return incumbent
        weight = weight - weightDelta

    return incumbent


def improved_solution(goal, openList, weight, pathCost):
    closedList = set()
    # while there are nodes in the open list
    while openList:

        current = min(openList, key=lambda o: o.G + weight * o.H)

        openList.remove(current)
        closedList.add(current)

        # exits function if estimated travel is more than best path cost
        if pathCost < current.G + weight * current.H:
            # pathCost is proven to be w-admissable
            return None

        # for each child
        for node in current.children:
            # Duplicate detection and updating g(n`)
            if node.isObstacle:
                continue
            if node in closedList and node.G < current.G + node.cost():
                continue
            if node in openList and node.G < current.G + node.cost():
                continue
            if current.parent:
                current.G = current.parent.G + current.cost()

            # Prune nodes over the bound
            if node.G + node.H > pathCost:
                continue
            if node in openList:
                new_g = current.G + node.cost()
                if node.G > new_g:
                    node.G = new_g
                    node.parent = current
            else:
                node.parent = current
                node.G = current.G + node.cost()
                if not node == goal:
                    node.H = ED(node, goal)
                else:
                    node.H = 1
                    path = []
                    while node.parent:
                        node = node.parent
                        path.append(node)
                    path.append(node)
                    return path[::-1]
                openList.add(node)
    return None
