from . import Algorithms
import pygame as p
import sys, os
# sys.pa\\th.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')))
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from UI.BoardType import Type as BT

class Dijkstra(Algorithms):

    def __init__(self, screen : p.Surface, Board : BT):
        super().__init__(screen, Board)

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
        else: self.selfGrid(inp[3])

    def thisGrid(self, Start : tuple, finish : tuple, row : int, col : int):
        import heapq as hq
        from UI.Grid import Grid as gG

        q = [(0, Start[0], Start[1], [Start])]
        Grid: gG = self.board
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
        return -1
    def selfGrid(self, Queue : list):

        return



def solution(finish : tuple, board : list[list]) -> int:
    # name : datatype
    # 3 버젼 부터 가능합니다
    # -> 이거 return data type 정해주는 겁니다
    # 이러면 속도가 더 빨라용
    import heapq as hq
    q = [(0, 0, 0)] # cost, (y,x)
    dx, dy = [0,0,1,-1],[1,-1,0,0]
    while q:
        cost, y, x = hq.heappop(q)
        if (y, x) == finish: return cost

        if board[y][x] <= cost: continue

        board[y][x] = cost;

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i];
            if 0 <= ny < len(board) and 0<= nx < len(board[0]) and board[ny][nx] != -1:
                # -1을 장애물이라고 생각해주세요
                hq.heappush(q, (cost+1, ny, nx))
    return -1
