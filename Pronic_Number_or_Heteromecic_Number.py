t=int(input())
c=0
s=1
for i in range(0,t+1):
    if i*(i+1)==t:
        c=1
if c==1:
    print("YES")
else:
    print("NO")