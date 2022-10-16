t=int(input())
l=list(map(int,input().split()))
a=int(input())
x=l.index(a)
s=0
for i in range(0,x+1):
    s+=l[i]
print(s)