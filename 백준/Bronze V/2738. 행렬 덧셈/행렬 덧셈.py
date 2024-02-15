N,M = map(int, input().split())
A,B=[],[]
for i in range(N):
    A.append([int(x) for x in input().split()])
for i in range(N):
    B.append([int(x) for x in input().split()])

for i in range(N):
    for j in range(M):
        A[i][j]=A[i][j]+B[i][j]
        
for i in A:
    print(*i)