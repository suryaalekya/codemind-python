n=int(input())
for i in range(n):
    a=input()
    if a==a[::-1]:
        print("True")
    else:
        print("False")