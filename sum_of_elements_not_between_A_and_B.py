n=int(input())
l=list(map(int,input().split()))
l.sort()
m,k=map(int,input().split())
s=0
c=0
for i in range(0,n):
    if l[i] in range(m,k+1):
        pass
    else:
        c+=l[i]
print(c)