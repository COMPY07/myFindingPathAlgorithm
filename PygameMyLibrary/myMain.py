
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
        self.food_market : list= []
    def __eq__(self, other):
        # eqaul 입니다.. 객체를 비교할때 무엇을 보고 같다고 판단할지를 넘겨주는 거에용
        return self.position == other.position
    def __cmp__(self, other):
        return self.f > other.f
    def __lt__(self, other):
        return self.f < other.f

def heuristic(node, goal, D=1, D2=2 ** 0.5):  # Diagonal Distance
    dx = abs(node.position[0] - goal.position[0])
    dy = abs(node.position[1] - goal.position[1])
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)




def aStar(board, start, end):
    # startNode와 endNode 초기화
    import heapq

    # 밀집도, 성향, 거리 순으로 가중치 부여, * (3 - idx);


    startNode : Node = Node(None, start)
    endNode : Node = Node(None, end)

    # openList, closedList 초기화
    openList : list = []
    closedList : list= []

    # openList에 시작 노드 추가
    openList.append(startNode)
    dx, dy = [0,0,-1,1,-1,-1,1,1], [-1,1,0,0,-1,1,-1,1]
    # endNode를 찾을 때까지 실행
    while openList:

        # 현재 노드 지정
        currentNode : Node= heapq.heappop(openList)
        # currentIdx = 0

        # 이미 같은 노드가 openList에 있고, f 값이 더 크면
        # currentNode를 openList안에 있는 값으로 교체
        '''for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIdx = index

        # openList에서 제거하고 closedList에 추가
        openList.pop(currentIdx)'''
        closedList.append(currentNode)

        # 현재 노드가 목적지면 current.position 추가하고
        # current의 부모로 이동
        if currentNode == endNode:
            path = []
            food_markets = []
            current = currentNode
            while current is not None:
                y, x = current.position
                board[y][x] = current.f
                path.append(current.position)
                food_markets+=current.food_market
                print("위치 : ", current.position)  # 휴리스틱
                current = current.parent

            return path[::-1], food_markets  # reverse
            # heapq 쓰면 reverse 안해도 되용

        children : list = []

        for i in range(8):
            ny, nx = currentNode.position[0] + dy[i], currentNode.position[1] + dx[i]

            # 범위 체크
            if 0 > ny or ny >= len(board) or\
                0 > nx or nx >= len(board[0]):
                continue
            if board[ny][nx] != 0:
                if board[ny][nx] == 2: currentNode.food_market.append((ny, nx))
                continue

            new_node : Node = Node(currentNode, (ny, nx))
            children.append(new_node)

        for child in children:

            if child in closedList: continue

            # f, g, h값 업데이트
            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) +\
                      ((child.position[1] - endNode.position[1]) ** 2) # 퓌타고라스
            # child.h = heuristic(child, endNode) 다른 휴리스틱
            # 위에거는 x, y 최대값을 이용해서 거리를 구하는 Diagonal Distance 입ㄴ디ㅏ.

            # print("위치 : ", child.position) # 휴리스틱
            # print("목표 로부터 거리 : ", child.h)

            child.f = child.g + child.h

            # 자식이 openList에 있고, g값이 더 크면 continue
            flag : bool = False
            for node in openList:
                if child == node and child.g > node.g:
                    flag = True
                    break
            if flag: continue

            heapq.heappush(openList, child)
        # 요 기다가 밀집도 및 다른 변수 넣어서 처리하기로


def main():
    # 1은 장애물

    myMap = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    start = (0, 0) # 현재 사용자의 위치를 노드의 위치로 변환
    end = (0, 9) # 등록된 놀이기구의 위치를 목표 노드로 설정


    path = aStar(myMap, start, end) # A* 알고리즘 시작
    print(path) # # 경로 return
    # print(board)


# [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
# [0, 62, 0, 0, 1, 0, 0, 0, 0, 0],
# [0, 0, 43, 0, 1, 0, 0, 0, 0, 0],
# [0, 0, 0, 28, 1, 0, 0, 0, 0, 0],
# [0, 0, 0, 22, 1, 0, 0, 0, 0, 0],
# [0, 0, 0, 18, 1, 0, 0, 0, 0, 0],
# [0, 0, 0, 16, 1, 0, 0, 0, 0, 0],
# [0, 0, 0, 16, 1, 0, 11, 0, 0, 0],
# [0, 0, 0, 18, 1, 12, 0, 0, 0, 0],
# [0, 0, 0, 0, 17, 0, 0, 0, 0, 0]]



import pygame as p
Running = True
from UI.Grid import Grid as grid

Grid : grid = grid()
