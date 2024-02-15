K = int(input())
write =[]
for _ in range(K):
    word = int(input())
    if word == 0:
      write.pop()
    else:
      write.append(word)
print(sum(write))