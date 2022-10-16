t=input()
s='qwertyuiopasdfghjklzxcvbnm'
c=0
for i in range(0,len(t)):
    if t[i] in s:
        c+=1
print(c)