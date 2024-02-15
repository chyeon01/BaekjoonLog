first = int(input())
second = int(input())
A = second//100
B = (second%100)//10
C = second%10
third = first*C
forth = first*B
fifth = first*A
print(third)
print(forth)
print(fifth)
print(fifth*100 + forth*10 + third)
