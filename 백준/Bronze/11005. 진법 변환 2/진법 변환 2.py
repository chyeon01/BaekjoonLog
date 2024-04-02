N,B = map(int,input().split())
alp=[]
for a in range(65,91):
    alp.append(chr(a))
    
L=[]
while True:
    L.append(int(N%B))
    N=N//B
    if N==0:
      break

Last=[]
for l in L:
    if l>=10:
        Last.append(alp[l-10])
    else:
        Last.append(l)

for i in Last[::-1]:
    print(i, end="")