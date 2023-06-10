import pygame as p
from BoardType import Type as Type
from Box import Box as Box


class Grid(Type):

    def __init__(self, screen: p.Surface = None,
                 row: int = 5, col: int = 5,
                 space: float = -1.5):

        super().__init__(screen, row, col)

        self.space = space
        self.board: list = list()  # [[0 for i in range(row)] for i in range(col)]

        (sc_width, sc_height) = screen.get_size()

        self.bx_width = sc_width // row
        self.bx_height = sc_height // col

        for i in range(row):
            self.board.append(list())

            for j in range(col):
                self.board[i].append(Box(i * self.bx_width, j * self.bx_height,
                                         self.bx_width + space, self.bx_height + space))  # x, y, width, height, color

    def boardUpdate(self, delay: int):
        self.screen.fill(self.WHITE)

        for i in self.board:
            for j in i:
                j.draw(self.screen, p)
        p.display.flip()

        p.time.delay(delay)

    def Colors(self):
        cnt: int = 0

        for name, rgb in self.custom_color.items():
            cnt += 1
            print(f"{name}의 rgb값은 {rgb}  ", end='')
            if cnt // 3 == 1:
                cnt = 0
                print()

    def changeColor(self, *inp):
        res: str = super().changeColor(inp)
        if not res: return False
        for i in self.board:
            for box in i:
                if box.colorName != res: continue
                box.colorName = inp[1]
                box.color = self.custom_color[inp[1]]
        return True

    def changeBox(self, *inp):
        # x: int, y: int, color=0):
        box: Box

        if len(inp) > 2:
            x, y = inp[0], inp[1]
            box = self.board[y][x]

            if type(inp[2]) == int:
                color: int = inp[2]
            else:
                color: str = inp[2]
        else:
            box = inp[0]

            if type(inp[1]) == int:
                color: int = inp[1]
            else:
                color: str = inp[1]
        # print(inp, box, color)
        if type(color) == int:
            box.colorName = self.color_idx[color]
            box.color = self.custom_color[box.colorName]

        elif type(color) == str:
            box.colorName = color
            box.color = self.custom_color[color]

        else:
            return False
        return True

    def getBoxbyCoordinate(self, x: int, y: int):
        return self.board[x // self.bx_width][y // self.bx_height]

    def getBoxbyIndex(self, x: int, y: int):
        return self.board[y][x]

    def getBox(self, x: int, y: int):
        return self.getBoxbyCoordinate(x, y)
