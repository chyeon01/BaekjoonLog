N,M=map(int,input().split())
L=[0 for i in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    for x in range(a-1,b):
        L[x]=c
print(" ".join(map(str,L)))
        