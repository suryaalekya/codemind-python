t=int(input())
c=0
i=1
while i<=t:
    if t%i==0:
        c+=1
    i+=1
if c==2:
    print("prime")
else:
    print("not a prime")