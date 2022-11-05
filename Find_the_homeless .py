n=int(input())
p=[]
h=[]
for i in range(n):
    p.append(int(input()))
for i in range(n):
    h.append(int(input()))
c=0
for i in range(n):
    if(p[i]>h[n-1]):
        c+=1
print(c)