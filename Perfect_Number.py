t=int(input())
i=1
c=0
while i<t:
    if t%i==0:
        c+=i
    i+=1
if c==t:
    print("True")
else:
    print("False")
