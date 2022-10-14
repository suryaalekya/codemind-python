n=int(input())
list=map(int,input().split())
s=0
for i in list:
    if i%2==1:
        s+=i
print(s)
        