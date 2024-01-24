import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def sorting():
  if len(arr) == m:
    print(*arr)
    return
  for i in range(1, n + 1):
    if i in arr:
      continue
    arr.append(i)
    sorting()
    arr.pop()

sorting()