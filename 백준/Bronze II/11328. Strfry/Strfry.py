N = int(input())
for i in range(N):
    text_1, text_2 = input().split()
    if  sorted(text_1) == sorted(text_2):
        print("Possible")
    else:
        print("Impossible")
    