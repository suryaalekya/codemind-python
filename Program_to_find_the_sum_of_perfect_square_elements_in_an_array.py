import math
n=int(input())
l=list(map(int,input().split()))
#print(l)
c=0
for i in l:
    r=int(math.sqrt(i))
    if r*r==i:
        c+=i
print(c)