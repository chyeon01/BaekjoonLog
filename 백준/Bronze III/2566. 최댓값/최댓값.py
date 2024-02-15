b=[]
c=[-1,-1]
a = [[int(x) for x in input().split()]for i in range(9)]
for x in range(9):
    b.append(max(a[x]))
c[0] = b.index(max(b))+1
c[1] = a[c[0]-1].index(max(b))+1
print(max(b))
print(*c)