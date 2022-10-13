t=int(input())
s=str(t*t)
t=str(t)
if s.endswith(t):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")