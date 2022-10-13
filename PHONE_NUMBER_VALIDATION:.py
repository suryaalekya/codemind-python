s=input()
a=s.startswith('1')
b=s.startswith('2')
c=s.startswith('3')
d=s.startswith('4')
e=s.startswith('5')
f=s.startswith('6')
g=s.startswith('7')
h=s.startswith('8')
i=s.startswith('9')
if len(s)==10 and (a or b or c or d or e or f or g or h or i):
    print("Valid")
else:
    print("Invalid")