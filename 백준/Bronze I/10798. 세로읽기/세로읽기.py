a=[0,0,0,0,0]
for i in range(5):
    a[i]=list(input())
c=""
for i in range(15):
    for x in range(5):
        try:
            c+=a[x][i]
        finally:
            continue
    x=0
print(c) 
