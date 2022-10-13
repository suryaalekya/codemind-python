t=input()
s=t[::-1]
t=int(t)
s=int(s)
x=t*t
y=s*s
p=str(y)
if str(x)==p[::-1]:
    print("True")
else:
    print("False")