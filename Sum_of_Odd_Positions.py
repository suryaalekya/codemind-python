n=int(input())
l=list(map(int,input().split()))
o=0
for i in range(0,n):
    if i%2!=0:
        o+=l[i]
print(o)   