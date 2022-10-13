n=int(input())
t=n
n=abs(n)
r=0
while n>0:
    s=n%10
    r=r*10+s
    n=n//10
if t>0:
    print(r)
elif t<0:
    print(-(r))