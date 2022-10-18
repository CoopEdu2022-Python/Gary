def huiwen(s):
    s=''
    for i in s:
        if i.isalnum():
            s+=i.lower()
    return s==s[::-1]



