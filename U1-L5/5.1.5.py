a = ['cd',34,567,45,4567,89067,789]
b=[]
c=0
for i in a:
    if type(i)== int or type(i)== float:
        c=int(i)*2

        b.append(c)
    else:
        b.append(i)
print(b)
