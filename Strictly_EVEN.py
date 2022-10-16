n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,n):
    if l[i]%2==0:
        if i%2==0:
            pass
        else:
            s=1
if s==0:
    print("True")
else:
    print("False")
    