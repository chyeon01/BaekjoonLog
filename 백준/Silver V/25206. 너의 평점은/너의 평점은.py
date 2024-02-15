score = 0
number = 0
for i in range(20):
    a,b,c = input().split()
    b=float(b)
    number+=b
    if c=='A+':
        c=4.5
    elif c=='A0':
        c=4.0
    elif c=='B+':
        c=3.5
    elif c=="B0":
        c=3.0
    elif c=="C+":
        c=2.5
    elif c=="C0":
        c=2.0
    elif c=="D+":
        c=1.5
    elif c=="D0":
        c=1.0
    elif c=="F":
        c=0.0
    elif c=="P":
        c=0.0
        number-=b
    score += b*c
print(score/number)
     