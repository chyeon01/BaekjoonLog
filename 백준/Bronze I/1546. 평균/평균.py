N = int(input())
score = [int(x) for x in input().split()]
ave=0
M = max(score)
for i in score:
    ave+=i/M*100
print(ave/len(score))