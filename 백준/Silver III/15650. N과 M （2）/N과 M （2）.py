import sys
from itertools import combinations
#permutations, combinations, product 차이 구분 잘하기

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

for seq in combinations(arr, m):
    print(*seq)