t=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,t):
    if l[i]!=0 and l[i]!=1:
        s=1
        break
if s==1:
    print("False")
else:
    print("True")