num = int(input())

for i in range(num):
    word=input()
    bracket=[]
    
    for j in word:
        if j=="(":
            bracket.append(j)
        elif j==")":
            if len(bracket)!=0 and bracket[-1]=="(":
                bracket.pop()
            else:
                bracket.append(")")
                break
    if len(bracket) ==0:
        print("YES")
    else:
        print("NO")