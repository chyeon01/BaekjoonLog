import sys
input = sys.stdin.readline

n= int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,input().rstrip().split())))

answer = {-1:0, 0:0, 1:0}

def dfs(x,y,n):
    stand = paper[x][y] #가장 첫번째를 기준으로 다르면
    for i in range(x,x+n): 
        for j in range(y,y+n):
            if paper[i][j] != stand:
                n //= 3 #9등분
                dfs(x,y,n) #첫번째 행
                dfs(x,y+n,n)
                dfs(x,y+2*n,n)

                dfs(x+n,y,n) # 2행
                dfs(x+n,y+n,n)
                dfs(x+n,y+2*n,n)
                    
                dfs(x+2*n,y,n) # 3행
                dfs(x+2*n,y+n,n)
                dfs(x+2*n,y+2*n,n)
                return
    answer[stand]+=1 # 다 돌았는 데 같으면 해당 되는 것에 +1

dfs(0,0,n)

for i in answer.values():
    print(i)