from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
queue = deque()

for i in range(N):
    cmd = sys.stdin.readline().rstrip()
    
    if cmd=='pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
            
    elif cmd=='size':
        print(len(queue))
        
    elif cmd=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    
    elif cmd=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            
    elif cmd=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
    else:
        cmd,X = cmd.split()
        queue.append(int(X))