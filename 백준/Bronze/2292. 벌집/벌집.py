N = int(input()) - 1
i = 1
while True:
    if N <= 0:
        break
    N = N-(6*i)
    i += 1
print(i)