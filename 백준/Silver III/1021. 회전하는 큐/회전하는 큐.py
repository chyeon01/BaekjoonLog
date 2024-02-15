from collections import deque

N,M = map(int, input().split())

Queue = deque(n for n in range(1,N+1))
index = [int(x) for x in input().split()]

count = 0
for i in index:
    while True:
        if Queue[0]==i:
            Queue.popleft()
            break
        else:
            if Queue.index(i) <=len(Queue)//2:
                Queue.rotate(-1)
                count+=1
            else:
                Queue.rotate(1)
                count +=1
print(count)