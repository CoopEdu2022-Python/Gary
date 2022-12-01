a = open('bad_boy.py', 'r+')
b=a.readlines()
c=[]
for i in range(len(b)):
    if b[i].startswith('    '):
        c.append(b[i])
    elif b[i].startswith('   '):
        c.append(b[i][1:])
    else:
        c.append(b[i])
print(c)