def isbal(s):
    while(True):
        if '[]' in s:
            s=s.replace('[]','')
        elif '()' in s:
            s=s.replace('()','')
        elif '{}' in s:
            s=s.replace('{}','')
        else:
            return not s
s= input()
if isbal(s):
    print('True')
else:
    print('False')