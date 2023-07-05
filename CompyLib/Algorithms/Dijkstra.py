# 21 05 21
import sys


def solution_1():
    return


# print(solution_1())

# #############################################################

# TSP
# visualization

# turtle, pygame 으로도 가능하다

import pygame, sys, os
# from tkinter import *

win_width, win_height = 400, 400  # 가로 세로 400 400
rows, cols = 8, 8  # 세로 가로 / 행과 열
# 8*2 = 64 개의 grid
win = pygame.display.set_mode((win_width, win_height))  # (width, height)
pygame.display.set_caption("(그리드 & 다익스트라) 알고리즘")
grid_width, grid_height = win_width // cols, win_height // rows
#                         400 // 4,           400 // 4

target_flag = False  # 목표물이 설정되지 않은 상태
WHITE = (255, 255, 255)  # r, g, b


class Box:
    # constructor.. 박스가 박스이기 위한.. 필요한 것들이 뭐가 있나
    # __init__
    # 필요한것
    # x, y 좌표(위치)
    # start, goal, wall인지
    def __init__(self, x, y, block_width, block_height):
        self.x, self.y = x, y
        self.color = (0, 255, 0)

        self.cost = float('inf')

        self.width, self.height = block_width, block_height
        self.start, self.goal, self.wall = False, False, False
        self.path = False
        self.visited = False

    # class 특징
    # variables 초기화 + methods
    # object의 statu 즉 가지고 잇는 변수 s ex) 키가 몇이다.. 눈의 색깔이 무엇이다
    # object의 behavior .. 행동... 함수... method= fuction = 함수
    # 여기선 어떤 함수가 필요한가

    # 박스를 그려야지
    # pygame.draw.rect(도화지 이름, 색깔(r, g, b), (a, b, c, d))
    # a,b는 한점 x, y, c는 width, d는 height
    # 즉 (x, y, width, height)
    def setcolor(self, color): self.color = color

    def draw(self, mywin):
        # color = (0, 255, 0)
        pos = (self.x, self.y, self.width - 2.5, self.height - 2.5)
        pygame.draw.rect(mywin, self.color, pos)

def dij(g, finish_x, finish_y):
    result_path = []
    result_cost = float('inf')
    q = [(0, 0, 0, [], g[0][0])]
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    xlen, ylen = len(g[0]), len(g)
    while q:
        x, y, cost, path, bx = q.pop()
        if bx.wall == True or \
                result_cost <= cost or bx.cost <= cost: continue
        g[x][y].cost = cost
        bx.cost = cost
        if (x, y) == (finish_x, finish_y):
            if result_cost > cost:
                result_cost = cost
                result_path = path
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < xlen and 0 <= ny < ylen:
                q.append((nx, ny, cost + 1, path + [(x, y)], g[nx][ny]))
    return result_path if result_cost != float('inf') else None

def makit():
    global target_flag
    # 그래픽 처리는 무조건 refresh 화면을 계속 찍는것
    g = []  # grids
    for i in range(cols):
        temp = []
        for j in range(rows):
            temp.append(Box(i * grid_width, j * grid_height, grid_width, grid_height))  # object 넣기
        g.append(temp)
    start_box = g[0][0]
    start_box.visited = True
    start_box.start = True
    start = False
    q = [start_box]
    target_pos = (0, 0)
    isRun = True
    while isRun:
        # 이벤트.. 이벤트 프로그래밍..  in cs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # system
            elif event.type == pygame.MOUSEMOTION:
                position = pygame.mouse.get_pos()  # (x, y) 현재 마우스의 위치를 return함 tuple의 형태로
                x, y = position
                x, y = x // grid_width, y // grid_height
                if event.buttons[0]:  # 왼쪾 마우스가 클릭되면
                    print(f"방해물 설정 중 : 좌표 x = {x}, y = {y}")
                    if (x, y) == target_pos or (x, y) == (0, 0): continue
                    g[x][y].setcolor((255, 0, 0))
                    g[x][y].wall = True
                # 1번은 마우스 휠
                elif event.buttons[2] and target_flag == False:  # 오른쪽 마우스 클릭되면
                    print(f"목표물 설정 : 블럭 좌표 x = {x}, y = {y}")
                    g[x][y].setcolor((0, 0, 255))
                    g[x][y].goal = True
                    target_pos = (x, y)
                    target_flag = True
            elif event.type == pygame.KEYDOWN and target_flag == True:  # 키가 눌렸다면 실행
                print('알고리즘 시작')
                start = True
                g[0][0].start = True
                isRun = False
                nf = dij(g, target_pos[0], target_pos[1])
                if nf == None: return "경로 없음"
                else:
                    for (x,y) in nf:
                        g[x][y].setcolor((0,0,0))

        for i in g:
            for j in i:
                j.draw(win)

        # win.fill(WHITE) #(r,g,b)
        # pygame.display.update(win)
        pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # system
        for i in g:
            for j in i:
                j.draw(win)
    return


print(makit())
