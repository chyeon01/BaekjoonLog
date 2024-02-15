from collections import deque
import sys

N,K = map(int, input().split())
load = [0]*100001 #거리 겸 시간

Queue = deque()
Queue.append(N)

while Queue:
    x = Queue.popleft()
    if x==K:
        print(load[x])
        break
    for go_x in (x-1, x+1, x*2):
        if 0<=go_x<=100000 and load[go_x] == 0: #범위안에서 가지 않은 곳만
            load[go_x] = load[x]+1
            Queue.append(go_x)