N,B = input().split()
alp={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}
L=[]
cnt = 0
i=0
for n in N:
    L.append(n)
L = L[::-1]
for l in L:
    if l in alp.keys():
        l=alp[l]
    l = int(l)
    cnt += l*(int(B)**i)
    i+=1
print(cnt)