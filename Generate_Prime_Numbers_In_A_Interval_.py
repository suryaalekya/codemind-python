a=int(input())
b=int(input())
for j in range(a+1,b+1):
    n=j
    is_prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(n)