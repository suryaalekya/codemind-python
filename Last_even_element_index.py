t=int(input())
s=0
l=list(map(int,input().split()))
for i in range(t-1,0,-1):
    if l[i]%2==0:
        s+=1
        break
if s==1:
    print(i)
else:
    print("0")