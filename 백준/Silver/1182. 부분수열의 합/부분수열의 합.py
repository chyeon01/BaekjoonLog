import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = [int(x) for x in input().strip().split()]
answer = []

cnt = 0
start=0

def sorting(start):#start 안 정해주면 무한 재귀
  global cnt
  if sum(answer) == s and len(answer)>0:
    cnt += 1
  for i in range(start,n):
    answer.append(arr[i])
    sorting(i+1)
    answer.pop()

sorting(start)
print(cnt)