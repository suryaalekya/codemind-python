n=int(input())
s=0
l=list(map(int,input().split()))
for i in range(0,n-1):
    if l[i]%2!=0:
        s=1
    else:
        continue
if s==1:
    print("False")
else:
    print("True")