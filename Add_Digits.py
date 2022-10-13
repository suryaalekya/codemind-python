t=int(input())
i=1
c=0
while t!=0:
    r=t%10
    c+=r
    t=t//10
    if t==0 and c>9:
        t=c
        c=0
print(c)