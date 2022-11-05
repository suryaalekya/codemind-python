def angle(h,m):
    if h==12:
      h=0
    if m==60:
      m=0
    if h>12:
        h+=1
        h=h-12
    h_a=0.5*(h*60+m)
    m_a=6*m
    a_l=abs(h_a-m_a)
    res=min(360-a_l,a_l)
    return res
n=input()
n=n.replace(':','')
l=list(map(int,n))
if l[0]==1:
    l[1]=l[1]+10
h=l[1]
m=l[2]*10+l[3]
print(angle(h,m))
      
