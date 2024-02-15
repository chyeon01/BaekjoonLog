word_1 = input()
word_2 = input()
count=0

for i in range(ord('a'),ord('z')+1):
  count += abs(word_1.count(chr(i))-word_2.count(chr(i)))

print(count)