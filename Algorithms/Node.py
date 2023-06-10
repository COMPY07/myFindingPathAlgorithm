class Node:
    def __init__(self, parent=None, position: tuple = None, state: int = 0, density: int = 0):
        self.parent = parent
        self.position: tuple = position

        self.g: float = float('inf')
        self.h: float = float('inf')
        self.f: float = float('inf')

        self.state: int = state
        self.density: int = density

        self.food_market: list = []

    def __eq__(self, other):
        # eqaul 입니다.. 객체를 비교할때 무엇을 보고 같다고 판단할지를 넘겨주는 거에용
        return self.position == other.position

    def __cmp__(self, other):
        return self.f > other.f

    def __lt__(self, other):
        return self.f < other.f

    def __str__(self):
        return f"위치 : {self.position}"
