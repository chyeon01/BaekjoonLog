h,m = map(int,input().split())
t=h*60+m-45
H = t//60
if H >=0:
    pass
else:
    H+=24
M = t%60
print(H,M)