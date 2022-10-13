a,b=map(str,input().split())
s=a[0:int(b)]
k=a[-(int(b)):]
print(abs(int(s)-int(k)))