t=input()
k='aeiou'
s=0
for i in range(0,len(k)):
    if k[i] not in t:
        s+=1
        print(k[i],end=' ')
if s==0:
    print("0")
        