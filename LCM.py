a,b=map(int,input().split())
i=1
while True:
    m=a*i  
    if m%b==0:
        print(m)
        break
    i+=1