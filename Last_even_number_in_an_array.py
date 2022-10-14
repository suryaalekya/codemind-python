t=int(input())
s=0
l=list(map(int,input().split()))
for i in range(t-1,-1,-1):
    if l[i]%2==0:
        print(l[i])
        break
    else:
        continue
 