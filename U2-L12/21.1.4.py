a = open('2.txt', 'r+')
v=a.read()
c=[]
b=['1','2','3','4','5','6','7','8','9','0']
k= [i for i in v]
for i in range(len(k)):
    if k[i]=='1' and k[i+1]=='0':
        c.append(10)

    elif k[i-1]=='1' and k[i]=='0':
        continue
    elif k[i] in b:
        c.append(k[i])
t=[]
for f in c:
    t.append(int(f))
t.sort()
print(t)
a.close()

