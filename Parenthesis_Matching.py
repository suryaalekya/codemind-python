def check(s):
    n=[]
    o=['[','{','(']
    c=[']','}',')']
    for i in range(len(s)):
        if s[i] in o:
            n.append(s[i])
        elif s[i] in c:
            l=c.index(s[i])
            if len(n)>0 and o[l]==n[len(n)-1]:
                n.pop()
            else:
                return i+1
    if len(n)==0:
        return 0
    else:
        return len(s)+1
s=input()
print(check(s))