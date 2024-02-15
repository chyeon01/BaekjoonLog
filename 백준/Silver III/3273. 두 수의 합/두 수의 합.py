n = int(input())
arr = [int(x) for x in input().split()]
x = int(input())

count=0
arr.sort()

start = 0
end = n - 1
while start != end:
  if arr[start]+arr[end] == x:
    start +=1
    count+=1
  elif arr[start]+arr[end]>x:
    end -=1
  else :
    start +=1
  

print(count)