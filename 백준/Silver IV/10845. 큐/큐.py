import sys

N = int(sys.stdin.readline().rstrip())
queue=[]

for i in range(N):
    cmd = sys.stdin.readline().rstrip()
    
    if cmd=='pop':
        if len(queue) != 0:
            print(queue.pop())
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
            print(queue[len(queue)-1])
            
    elif cmd=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])

    else:
        cmd,X = cmd.split()
        queue.insert(0,X)