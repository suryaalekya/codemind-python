a=int(input())
s=str(a)
if '6' in s:
    l=list(s)
    e=l.index('6')
    l[e]='9'
    p=''.join(l)
    print(p)
else:
    print(a)