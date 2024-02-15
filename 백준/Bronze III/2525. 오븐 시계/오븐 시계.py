h,m =map(int,input().split())
t=int(input())
l= h*60+m+t
H = l//60
M = l%60
if H>=24:
    H-=24
print(H,M)