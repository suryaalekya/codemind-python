s=input()
l=list(s)
i=0
j=len(l)-1
while(i<j):
    if not l[i].isalpha():
        i+=1
    elif not l[j].isalpha():
        j-=1
    else:
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
strOut='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'.join(l)
print(strOut)