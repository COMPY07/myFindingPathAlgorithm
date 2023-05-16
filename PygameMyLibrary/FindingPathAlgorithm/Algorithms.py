import pygame as p
# import sys, os
# sys.pa\\th.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')))
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from UI.BoardType import Type as BT
class Algorithms:
    def __init__(self, screen : p.Surface, Board : BT):
        self.screen = screen
        self.board = Board
        self.Start : tuple
        self.Finish: tuple
    def Grid(self, *inp):
        # (start), (finish), board, Queue = None
        print(inp)

        start = inp[0]
        finish = inp[1]
        board = inp[2]

        yn : bool = len(inp) > 3

        self.Start = start
        self.Finish = finish

        if yn: self.thisGrid(len(board[0]), len(board))
        else: self.selfGrid(inp[3], inp[2])
    def thisGrid(self, Start : tuple, finish : tuple, row : int, col : int):
        return
    def selfGrid(self, Queue : list, board : list):
        return


'''
    def dijkstraGrid(self, Start: tuple, finish: tuple, row : int, col : int):
        import heapq as hq
        q = [(0, Start[0], Start[1], [Start])]
        Grid : gG = self.board
        getbox = Grid.getBoxbyIndex
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        while q:
            cost, x, y, path = hq.heappop(q)
            currentBox = getbox(x, y)
            if currentBox.cost <= cost: continue
            currentBox.cost = cost
            Grid.changeBox(currentBox, "GREEN")
            if (x, y) == finish: return path
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < row and 0 <= ny < col:
                    hq.heappush(q, (cost + 1, nx, ny, path + [(nx, ny)]))
            Grid.boardUpdate(20)
        return "????"

'''