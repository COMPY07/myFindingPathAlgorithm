from FindingPathAlgorithm import *
from UI import *

row: int
col: int
width: int
height: int
board : list

def __init__(Row : int, Col : int,
             Width : int, Height : int,
             Board : list = None):
    global row, col, width, height, board
    row = Row
    col = Col
    width = Width
    height = Height
    board = Board
row = 20
col = 20
import pygame as pg
pg.init()
screen = pg.display.set_mode([500, 500])
myGrid = Grid(screen, row, col)
mydij = Dijkstra(screen, myGrid)
q = []
# mydij.Grid((0,0), (4,4), myGrid)


general_color = "BLUE"
mystart = AStar(screen, myGrid)
mystart.thisGrid((0,0),(10,10), myGrid.row, myGrid.col)
def sol():
    import heapq as hq
    global myGrid, row, col

    q = [(0, 10, 11, [(0, 0)])]

    getbox = myGrid.getBoxbyIndex
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while q:
        cost, x, y, path = hq.heappop(q)
        currentBox = getbox(x, y)
        if currentBox.cost <= cost: continue

        currentBox.cost = cost
        myGrid.changeBox(currentBox, "GREEN")

        if (x, y) == (row-1,col-1): return path
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                hq.heappush(q, (cost + 1, nx, ny, path + [(nx, ny)]))
                box = getbox(nx, ny)
                if box.colorName == general_color: myGrid.changeBox(getbox(nx, ny), "RED")
        myGrid.boardUpdate(20)
sol()

'''
myGrid = Grid.Grid(None, row, col)
myui = Ui.UI(width, height, row, col, myGrid)
myGrid.screen = myui.screen

'''