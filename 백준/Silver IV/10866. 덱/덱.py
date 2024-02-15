from collections import deque
import sys

Deque = deque()
N=int(sys.stdin.readline().rstrip())

for i in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    
    if cmd[0]=="push_front":
        Deque.appendleft(cmd[-1])
        
    elif cmd[0]=="push_back":
        Deque.append(cmd[-1])
        
    elif cmd[0]=="pop_front":
        if len(Deque)!=0:
            print(Deque.popleft())
        else:
            print(-1)
            
    elif cmd[0]=="pop_back":
        if len(Deque)!=0:
            print(Deque.pop())
        else:
            print(-1)
            
    elif cmd[0]=="size":
        print(len(Deque))
        
    elif cmd[0]=="empty":
        if len(Deque)!=0:
            print(0)
        else:
            print(1)
            
    elif cmd[0]=="front":
        if len(Deque)!=0:
            print(Deque[0])
        else:
            print(-1)
            
    elif cmd[0]=="back":
        if len(Deque)!=0:
            print(Deque[-1])
        else:
            print(-1)
            