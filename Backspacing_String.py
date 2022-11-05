def compare(s,t):
    def backspace(str):
        a=[]
        for i in str:
            if i!="#":
                a.append(i)
            else:
                if len(a):
                    a.pop()
        return "".join(a)
    s,t=backspace(s),backspace(t)
    return s==t
s=input()
t=input()
if(compare(s,t)):
    print("True")
else:
    print("False")
        