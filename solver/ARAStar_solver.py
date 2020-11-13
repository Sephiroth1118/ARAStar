import time


def ARAStar_solver(start, goal):
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
