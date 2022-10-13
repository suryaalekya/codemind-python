t=int(input())
a=0
b=1
s=0
for i in range(1,100):
    c=a+b
    if c==t:
        s=1
        break
    else:
        a=b
        b=c
if s==1:
    print("True")
else:
    print("False")