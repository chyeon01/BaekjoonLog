N,M = map(int,input().split())
L=[x+1 for x in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    L[a],L[b]=L[b],L[a]
print(*L)