t=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,t):
   while (l[i]!=0):
       r=l[i]%10
       s+=r
       l[i]=l[i]//10
print(s)