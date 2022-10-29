t=int(input())
for i in range(t):
    def prime(num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    def run(n,x):
        while prime(n)==False:
            n+=x
        return n
    n=int(input())
    pp=run(n,-1)
    np=run(n,1)
    if (n-pp)==(np-n):
        print(pp)
    elif (n-pp)<(np-n):
        print(pp)
    else:
        print(np)