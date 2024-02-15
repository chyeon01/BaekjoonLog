L=input()
L = L.upper()
S=set(L)
counter =[-1,-1]
for i in S:
    if L.count(i)==counter[1]:
        counter[0]="?"
    if L.count(i)>counter[1]:
        counter[0]=i
        counter[1]=L.count(i)
print(counter[0])
