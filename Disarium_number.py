n=int(input())
t=n
s=0
i=len(str(n))
while (n!=0):
    r=n%10
    s+=r**i
    i-=1
    n=n//10
if s==t:
    print("True")
else:
    print("False")