class Box:
    def __init__(self, x: float, y: float, width: float,
                 height: float, cost: float = float("inf"), color: tuple = (0, 0, 255), color_name: str = "BLUE"):

        self.x = x
        self.y = y

        self.color = color
        self.colorName = color_name

        self.width = width
        self.height = height
        self.cost = cost

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])  # x, y, width, height

    def __str__(self):
        return f"좌표 : {self.x}, {self.y}    두께 및 높이 : {self.width}, {self.height}    색 : {self.colorName}   가중치 : {self.cost}"
