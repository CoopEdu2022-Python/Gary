a = open('4.txt', 'r+')
b = a.read()
words='abcdefghijklmnopqrstuvwxyz'
words2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
v=[]
for i in b:
    if i in words:
        v.append(words2[words.index(i)])
    elif i in words2:
        v.append(words[words2.index(i)])
    else:
        v.append(i)
a.close()
a = open('4.txt', 'w')
a.writelines(v)
a.close()