n=int(input())
t=n
s=0
while n!=0:
    f=1
    r=n%10
    for i in range(1,r+1):
        f*=i
    s+=f
    n=n//10
if s==t:
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")