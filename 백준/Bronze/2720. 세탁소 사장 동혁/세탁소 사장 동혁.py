T = int(input())
for t in range(T):
    C = int(input())
    cent_list=[]
    cent_list.append(int(C//25))
    C = int(C % 25)
    cent_list.append(int(C//10))
    C = int(C % 10)
    cent_list.append(int(C//5))
    C = int(C % 5)
    cent_list.append(int(C//1))
    print(*cent_list)