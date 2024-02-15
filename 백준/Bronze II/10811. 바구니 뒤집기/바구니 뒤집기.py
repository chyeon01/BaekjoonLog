N,M = map(int,input().split())
ist=[int(x+1) for x in range(N)]
for x in range(M):
    a,b = map(int,input().split())
    for i in range((b-a+1)//2):
        ist[a-1+i],ist[b-1-i]=ist[b-1-i],ist[a-1+i]
print(*ist)