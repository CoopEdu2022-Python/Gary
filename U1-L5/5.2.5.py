a = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24],
     [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
b=[]
c=[]
g=''
new=[]
for p in range(1,37):
    b.append(p)
c.append(b[:6])
c.append(b[6:12])
c.append(b[12:18])
c.append(b[18:24])
c.append(b[24:30])
c.append(b[30:36])
print(c)
for i in c:
    for y in range(6):
        print('%3d'%i[y],end='')
    print('\n')



