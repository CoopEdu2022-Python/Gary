

a = open('1.txt', 'r+')
b=[]
for i,z in enumerate(a.readlines()):
    if z.startswith('#'):
        pass
    else:
        b.append(z)
a.close()
a= open('1.txt', 'w')
a.writelines(b)


