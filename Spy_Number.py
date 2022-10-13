n=int(input())
s=0
c=1
while n!=0:
    a=n%10
    s+=a
    c=c*a
    n=n//10
if s==c:
    print("Spy Number")
else:
    print("Not Spy Number")