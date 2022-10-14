n=int(input())
l=map(int,input().split())
e=0
for i in l:
    if i%2==0:
        e+=i
print(e)   