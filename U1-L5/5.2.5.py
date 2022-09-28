a = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24],
     [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
b=[]
c=[]
g=''
new=[]
new0=[]
new1=[]
new2=[]
new3=[]
new4=[]
new5=[]
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
print(tuple(c))


for i in c:

    new0.append(i[0])
for i in c:

    new1.append(i[1])
for i in c:

    new2.append(i[2])
for i in c:

    new3.append(i[3])
for i in c:

    new4.append(i[4])
for i in c:

    new5.append(i[5])

new.append(new0)
new.append(new1)
new.append(new2)
new.append(new3)
new.append(new4)
new.append(new5)
print(tuple(new))
df=[]
for fg in c:
    sf=0
    for x in range(6):
        sf+=int(fg[x])
    df.append(sf)
print(tuple(df))
go=[]

for sd in new:
    ho = 0
    for ssdc in range(6):
        ho+=int(sd[ssdc])
    go.append(ho)
print(tuple(go))


