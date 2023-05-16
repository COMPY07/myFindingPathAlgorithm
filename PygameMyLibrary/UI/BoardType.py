import pygame as p
class Type:
    def __init__(self, screen : p.Surface = None, row : int = 5, col : int = 5):
        self.Running = True

        self.screen = screen
        self.row = row
        self.col = col

        if screen == None: self.Running = False

        self.RED : tuple = (255, 0, 0)
        self.BLUE : tuple = (0, 0, 255)
        self.GREEN : tuple = (0, 255, 0)
        self.BLACK : tuple = (255, 255, 255)
        self.WHITE : tuple = (0, 0, 0)

        self.custom_color : dict = {"RED" : self.RED, "BLUE" : self.BLUE, "GREEN" : self.GREEN,
                                    "BLACK" : self.BLACK, "WHITE" : self.WHITE}
        self.color_idx : list = ["BLUE", "RED", "GREEN", " BLACK", "WHITE"]


    def update(self):
        return

    def changeColor(self, *inp):
        length : int = len(inp[0])
        print(inp[0])
        inp = inp[0]
        if length < 2 or type(inp[1]) != str: return False

        if inp[1] not in self.custom_color.keys():
            if length < 3 or type(inp[2]) != tuple: return False
            self.custom_color[inp[1]] = inp[2]

        ret : str
        if type(inp[0]) == int:
            ret = self.color_idx[inp[0]]
            self.color_idx[inp[0]] = inp[1]
        elif type(inp[0]) == str:
            if inp[0] not in self.color_idx: return False
            ret = inp[0]
            self.color_idx[self.color_idx.index(inp[0])] = inp[1]
        else: return False

        return ret

    def addColor(self, name : str, color : tuple):
        if name == None or name == "": return False
        self.custom_color[name] = color
        return True


