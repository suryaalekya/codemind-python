s=input()
k='!@#$%^&*()_{}|?><][\:;~`.,'
g=0
for i in range(0,len(s)):
    if s[i] in k:
        g+=1
print(g)