import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
card = deque(int(i)+1 for i in range(N))

while len(card)!=1:
    card.popleft()
    card.append(card.popleft())
print(*card)