t=input()
k='aeiouAEIOU'
s=0
for i in range(0,len(t)):
    if t[i] in k:
        s+=1
print(s)