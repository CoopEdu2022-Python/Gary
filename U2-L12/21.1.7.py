import os
a = open('dldkj.txt', 'r+', encoding='utf-8')
b=open('qpeuwr.txt', 'r+', encoding='utf-8')
c=open('zmcxbvn.txt', 'r+', encoding='utf-8')
d=[]
d.append(a)
d.append(b)
d.append(c)
e=''
r=''

for i in range(3):
    e = d[i].readline()[0:-4]+'.txt'
    r=d[i].name
    
    os.renames(r,e)
    d[i].close()
