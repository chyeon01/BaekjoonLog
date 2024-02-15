import sys
input = sys.stdin.readline

n= int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,input().rstrip().split())))

answer = {0:0, 1:0}

def dfs(x,y,n):
    stand = paper[x][y] #가장 첫번째를 기준으로 
    for i in range(x,x+n): 
        for j in range(y,y+n):
            if paper[i][j] != stand:
                n //= 2 
                dfs(x,y,n) #첫번째 행
                dfs(x,y+n,n)

                dfs(x+n,y,n) # 2행
                dfs(x+n,y+n,n)

                return
    answer[stand]+=1 # 다 돌았는 데 같으면 해당 되는 것에 +1

dfs(0,0,n)

for i in answer.values():
    print(i)