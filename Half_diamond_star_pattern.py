n=int(input())
if n>2:
    for i in range(1,n+1):
        print("*"*i,end='
')
    for i in range(n-1,0,-1):
        print("*"*i,end='
')
else:
    print("The pattern is not possible")