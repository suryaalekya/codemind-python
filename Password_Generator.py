s=input()
l=[]
fs=''
l=s.split(',')
for i in l:
    temp=i.split(':')
    name=temp[0]
    num=temp[1]
    length=len(name)
    mx=0
    for d in num:
        if(int(d)<=length):
            if(mx<int(d)):
                mx=int(d)
    if mx==0:
        fs+='X'
    else:
        fs+=name[mx-1]
print(fs)