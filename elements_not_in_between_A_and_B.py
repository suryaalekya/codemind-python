n=int(input())
l=list(map(int,input().split()))
m,k=map(int,input().split())
s=0
for i in range(0,n):
    if l[i] in range(m,k+1):
        continue
    else:
        print(l[i],end=' ')
        s=1
if s==0:
    print('-1')