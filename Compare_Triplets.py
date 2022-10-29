a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
k=0
for i in range(0,len(a)):
    if a[i]>b[i]:
        s+=1
    elif  a[i]<b[i]:
        k+=1
print(s,k)
        