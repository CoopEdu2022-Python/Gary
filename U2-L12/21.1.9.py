a=open('1.txt', 'r+')
b=[]
for i in range(10):
    c=a.readline()

    b.append(c)

a.close()
a=open('12.txt', 'w')
a.writelines(b)
a.close()