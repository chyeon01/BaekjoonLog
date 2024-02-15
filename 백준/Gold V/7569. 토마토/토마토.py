from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = []
Queue = deque()

for z in range(H):
    box = []
    for x in range(N):
        box.append(list(map(int, input().split())))
        for y in range(M):
            if box[x][y] == 1:
                Queue.append((z, x, y))
    tomato.append(box)

dz = [0, 0, 0, 0, 1, -1]
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]

day = 0

while Queue:
    z, x, y = Queue.popleft()
    for i in range(6):
        gz = z + dz[i]
        gx = x + dx[i]
        gy = y + dy[i]
        if 0 <= gz < H and 0 <= gx < N and 0 <= gy < M and tomato[gz][gx][gy] == 0:
            Queue.append((gz, gx, gy))
            tomato[gz][gx][gy] = tomato[z][x][y] + 1
            if day < tomato[gz][gx][gy]:
                day = tomato[gz][gx][gy] -1
 
for z in range(H):
    for x in range(N):
        if 0 in tomato[z][x]:
            print(-1)
            exit()
print(day)