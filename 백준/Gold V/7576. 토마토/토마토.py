from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int, input().split())
tomato = [list(map(int, input().split())) for i in range(n)]
answer = 0
Queue = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            Queue.append([i,j])
         
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while Queue:
    x,y = Queue.popleft()
    for i in range(4): # 상하좌우
        go_x = x + dx[i]
        go_y = y + dy[i]
    
        if 0<=go_x<n and 0<=go_y<m: # 범위 내에서만
            if tomato[go_x][go_y]==0:
                tomato[go_x][go_y] = tomato [x][y] +1 #일 수 계산을 위해
                Queue.append([go_x,go_y])

for line in tomato:
    for each in line:
      if each ==0:
        print(-1)
        exit()
    answer = max(answer,max(line))

print(answer-1) # 1일부터 시작해서 -1