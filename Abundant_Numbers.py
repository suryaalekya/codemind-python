t=int(input())
i=1
s=0
while i<t:
    if t%i==0:
        s+=i
    i+=1
if s>t:
    print("True")
else:
    print("False")