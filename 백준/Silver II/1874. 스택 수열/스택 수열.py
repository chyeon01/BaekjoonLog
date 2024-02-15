n = int(input())
i =1
stack = [0]
cal = []

for _ in range(n):
  number = int(input())
  while True:
    if stack[-1] == number:
      stack.pop()
      cal.append("-")
      break
    else:
      if i != n+1:
        stack.append(i)
        cal.append("+")
        i += 1
      else:
        cal.append("NO")
        break

if "NO" in cal:
  print("NO")
else:
  for i in cal:
    print(i)