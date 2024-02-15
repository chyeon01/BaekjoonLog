N,k = map(int,input().split())
people=[str(x) for x in range(1,N+1)]
target_list =[]

target = k-1 # 타켓의 인덱스
for i in range(N):
  if target >= len(people):
    target = target % len(people)
  target_list.append(people.pop(target))
  target += k-1 # k번째씩 늘려가지만 한 사람씩 제외했기 때문에 -1


print("<"+", ".join(target_list)+">")
  
