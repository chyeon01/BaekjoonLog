A=int(input())
B=int(input())
C=int(input())

result=str(A*B*C)

for i in range(48,58):
    print(result.count(chr(i)))