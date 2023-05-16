import pygame
from .Grid import Grid as grid
import pygame as p
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from PygameMyLibrary.FindingPathAlgorithm import Algorithms


class UI:
    def __init__(self, width : int, height : int,
                 row : int, col : int, Grid : grid = None,
                 Algorithm : Algorithms = None):
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.Grid : grid = Grid
        p.init()
        self.screen = p.display.set_mode([width, height])
        self.algorithm = Algorithm
    def setBoard(self, Grid : grid):
        self.Grid = Grid
    def setAlgorihtm(self, Algorithm : Algorithms):
        self.algorithm = Algorithm
    def setupBoard(self):
        self.Grid = grid(self.screen, self.row, self.col, -1.5)

    def update(self, selfUpdate : bool = None):
        Grid = self.Grid
        while Grid.Running:
            for event in p.event.get():
                if event.type == p.QUIT: Grid.Running = False
                if event.type == p.MOUSEMOTION:
                    position = pygame.mouse.get_pos()
                    x, y = position
                    box = Grid.getBox(x, y)
                    if event.buttons[0]: Grid.changeBox(box, 1)
                if event.type == p.KEYDOWN:
                    if event.key == p.K_SPACE:
                        for x, y in self.algorithm.Grid((0, 0), (9, 9), self.row, self.col):
                            Grid.changeBox(x, y, "RED")
                            Grid.boardUpdate(10)

            Grid.boardUpdate(0)