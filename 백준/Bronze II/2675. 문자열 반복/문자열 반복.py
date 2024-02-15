T=int(input())
for i in range(T):
    text=""
    R,S=input().split()
    R=int(R)
    for x in S:
        text += x*R
    print(text)