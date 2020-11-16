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
