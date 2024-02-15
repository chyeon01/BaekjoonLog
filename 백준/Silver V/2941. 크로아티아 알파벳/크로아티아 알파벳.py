cro=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input()
count=0
for i in cro:
    if i in s:
        t=s.count(i)
        s=s.replace(i,"0")
        count+=t
s=s.replace('0',"")
count+=len(s)
print(count)