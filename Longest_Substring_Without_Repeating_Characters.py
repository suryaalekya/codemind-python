def check(s):
    '''
    n={}
    m,f=0,0
    for i in range(len(s)):
        if s[i] in n:
            f=max(f,n[s[i]]+1)
        n[s[i]]=i
        m=max(m,i-f+1)
    return m
    '''
    n=len(s)
    st=0
    maxlen=0
    pos={}
    pos[s[0]]=0
    for i in range(1,n):
        if s[i] not in pos:
            pos[s[i]]=i
        else:
            if pos[s[i]]>=st:
                cl=i-st
                if maxlen<cl:
                    maxlen=cl
                    start=st
                st=pos[s[i]]+1
            pos[s[i]]=i
    if maxlen<i-st:
        maxlen=i-st
        start=st
    return s[start:start+maxlen]
v=input()
l=[]
for i in v:
    if i.upper() not in l:
        l.append(i)
s=''
for i in l:
    s+=i
k=check(s)
print(k)if len(k)>=3 else print(-1)