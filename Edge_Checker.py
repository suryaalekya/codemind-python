a,b=map(int,input().split())
if abs(a-b)==1:
    print("Yes")
elif (a==1 or a==10) and (b==1 or b==10):
    print("Yes")
else:
    print("No")