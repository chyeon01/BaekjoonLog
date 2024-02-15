from collections import deque
import sys

R,C = map(int, input().split())
maze = []

hq = deque()
fq = deque()
human = [[0] * C for _ in range(R)]
fire = [[0] * C for _ in range(R)]
for i in range(R):
    maze.append(list(input().strip()))
    for j in range(C):
        if maze[i][j] == "J":
            hq.append((i, j))
            human[i][j] = 1
        elif maze[i][j] == "F":
            fq.append((i, j))
            fire[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while fq:
    r, c = fq.popleft()
    for d in range(4):
        go_x = r + dx[d]
        go_y = c + dy[d]
        if 0 <= go_x < R and 0 <= go_y < C:
            if maze[go_x][go_y] == "#" or fire[go_x][go_y] : # 불 시간 갱신X
                continue
            fire[go_x][go_y] = fire[r][c] + 1 #불이 퍼지는 속도
            fq.append((go_x, go_y))

while hq:
    r, c = hq.popleft()
    for d in range(4):
        go_x = r + dx[d]
        go_y = c + dy[d]
        if not (0 <= go_x < R and 0 <= go_y < C):
            print(human[r][c])
            exit()
        if maze[go_x][go_y] == "#" or human[go_x][go_y]:
            continue
        if fire[go_x][go_y] and human[r][c] + 1 >= fire[go_x][go_y]: # 사람이 불 보다 늦음
            continue
        human[go_x][go_y] = human[r][c] + 1
        hq.append((go_x, go_y))
    
print("IMPOSSIBLE")