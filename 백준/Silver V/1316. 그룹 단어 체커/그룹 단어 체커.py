N=int(input())
count=0

for x in range(N):
    L=[]
    s=input()
    t=""
    J=True
    for i in s:
        if t!=i:
            if i in L:
                J=False
                break
            else:
                L.append(i)
                t=i
    if J:
        count+=1

    
print(count)