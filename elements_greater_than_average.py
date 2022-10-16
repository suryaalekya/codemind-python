n=int(input())
l=list(map(int,input().split()))
sum=sum(l)//n
c=0
for i in range(0,n):
    if l[i]>=sum:
        c+=1
print(c)