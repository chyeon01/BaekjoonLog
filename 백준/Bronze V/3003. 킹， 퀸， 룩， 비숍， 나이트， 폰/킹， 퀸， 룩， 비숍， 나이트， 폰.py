O=[1,1,2,2,2,8]
W=[int(x) for x in input().split()]
R=[0,0,0,0,0,0]
for i in range(len(O)):
    R[i]=O[i]-W[i]
print(*R)