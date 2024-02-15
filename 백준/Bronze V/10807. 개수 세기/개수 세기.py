N=int(input())
L = [int(i)for i in input().split()]
v=int(input())
count =0
for i in L:
    if v==i:
        count +=1
print(count)