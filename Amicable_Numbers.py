def pro(num):
    f=0
    for i in range(1,num):
        if num%i==0:
            f+=i
    return f
a=int(input())
b=int(input())
if (pro(b)==a and pro(a)==b):
    print("Amicable")
else:
    print("Not Amicable")