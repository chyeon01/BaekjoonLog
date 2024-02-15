canvas = [[0]*100 for i in range(100)] 
n=int(input())
for i in range(n):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            canvas[i][j]=1
total =0            
for i in range(100):
    total+=canvas[i].count(1)
print(total)