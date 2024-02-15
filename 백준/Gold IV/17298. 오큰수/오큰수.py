import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().split()))
NGE = [-1]*N
stack = []

stack.append(0) # 인덱스
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)


print(*NGE)