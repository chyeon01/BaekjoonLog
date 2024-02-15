one, two = input().split()
one = one[::-1]
two = two[::-1]

one = int(one)
two = int(two)

if one > two:
    print(one)
else:
    print(two)