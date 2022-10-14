t=int(input())
e=0
o=0
while t>0:
    r=t%10
    if r%2==0:
        e+=1
    else:
        o+=1
    t=t//10
if o>0 and e>0:
    print("Mixed")
elif e==0 and o>0:
    print("Odd")
else:
    print("Even")
        