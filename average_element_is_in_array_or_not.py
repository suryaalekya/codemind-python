n=int(input())
l=list(map(int,input().split()))
k=sum(l)//n
if k in l:
    print("True")
else:
    print("False")