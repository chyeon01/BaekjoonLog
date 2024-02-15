N ,k = map(int, input().split())

room = [[0]*2 for i in range(6)]
count = 0

for i in range(N):
    S ,Y = map(int, input().split())
    if room[Y-1][S-1] == k:
        room[Y-1][S-1]=1
        count+=1
    else:
        room[Y-1][S-1]+=1

for i in room:
  count += 2 - i.count(0)
print(count)
    