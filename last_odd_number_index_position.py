t=int(input())
l=list(map(int,input().split()))
for i in range(t-1,0,-1):
    if l[i]%2!=0:
        print(i)
        break