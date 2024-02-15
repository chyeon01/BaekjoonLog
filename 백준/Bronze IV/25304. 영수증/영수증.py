total = int(input())
num = int(input())
real =0
for i in range(num):
    a,b =map(int,input().split())
    real += a*b
if total == real:
    print("Yes")
else:
    print("No")