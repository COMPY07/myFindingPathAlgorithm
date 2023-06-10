class Astar():
    def __init__(self, grid):
        self.grid = grid

    def heuristic_Diagonal_Distance(self, node, goal, D1=1, D2=2 ** 0.5):
        dx = abs(node.position[0] - goal.position[0])
        dy = abs(node.position[1] - goal.position[1])

        return D1 * (dx + dy) + (D2 - 2 * D1) * min(dx, dy)

    def heuristic_Euclidean_Distance(self, current, end):
        return ((current.position[0] - end.position[0]) ** 2) + ((current.position[1] - end.position[1]) ** 2)

    def CalcNode(self, currentNode, endNode):
        currentNode.g = currentNode.g + 1
        currentNode.h = self.heuristic_Euclidean_Distance(currentNode, endNode)
        currentNode.f = currentNode.g + currentNode.h + currentNode.density ** 2

    def NodeSet(self, node, g: int, f: int, h: int):
        node.g = g
        node.h = h
        node.f = f

    def getPath(self, node, board: list[list]):
        path = []
        while node != None:
            y, x = node.position
            board[y][x] = node.f
            path.append(node.position)
            node = node.parent
        return path[::-1]

    def AStar(self, board: list[list], start: tuple, end: tuple, delay: int = 0):
        import heapq as hq
        from Node import Node

        startNode = board[start[0]][start[1]]
        endNode = board[end[0]][end[1]]

        self.NodeSet(startNode, 0, 0, 0)

        openList: list[Node] = list()
        closedList: list[Node] = list()

        openList.append(startNode)
        dx, dy = [0, 0, -1, 1, -1, -1, 1, 1], [-1, 1, 0, 0, -1, 1, -1, 1]

        Visualization = self.grid != None

        while openList:
            currentNode: Node = hq.heappop(openList)
            closedList.append(currentNode)

            if Visualization:
                self.grid.changeBox(self.grid.getBoxbyIndex(currentNode.position[0],
                                                  currentNode.position[1]), "GREEN")

            if endNode == currentNode:
                return self.getPath(currentNode, board)

            # children: list[Node] = []

            for i in range(8):
                ny = currentNode.position[0] + dy[i]
                nx = currentNode.position[1] + dx[i]

                if 0 > ny >= len(board) or 0 > nx >= len(board[0]) or board[ny][nx].state == 1:
                    continue

                # children.append(board[ny][nx])

                child: Node = board[ny][nx]

                if child in closedList or child.g + child.density <= currentNode.g + 1:
                    continue
                self.CalcNode(child, endNode)
                child.parent = currentNode

                hq.heappush(openList, child)
            if Visualization: self.grid.boardUpdate(delay)
        return -1
