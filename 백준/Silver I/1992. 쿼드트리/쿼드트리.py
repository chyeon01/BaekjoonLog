n= int(input())
paper = []
for i in range(n):
    paper.append(list(input().rstrip()))

def dfs(x,y,n):
    stand = paper[x][y] #가장 첫번째를 기준으로 
    for i in range(x,x+n): 
        for j in range(y,y+n):
            if paper[i][j] != stand:
                print("(", end="")
                n //= 2 
                dfs(x,y,n) #첫번째 행
                dfs(x,y+n,n)

                dfs(x+n,y,n) # 2행
                dfs(x+n,y+n,n)
                print(")", end="")
                return
    
    print(stand, end="")

dfs(0,0,n)