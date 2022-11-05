def solve(str):
    import re
    d=list(set(re.findall("\d",str)))
    d.sort()
    d.reverse()
    n=int(''.join(d))
    if(n%2==0):
        print(n)
    else:
        l=len(d)
        for i in range(l-1,0,-1):
            if int(d[i])%2==0:
                ds=d[i]
                d.remove(ds)
                d.insert(l-1,ds)
                en=int(''.join(d))
                print(en)
                break
        else:
            print('-1')
str=input()
solve(str)
        