p=int(input('?'))
def a(p):
    l=[]
    v=[]
    er=0
    for i in range(7):
        g=int(input('?'))
        if g>10 or g<0:
            print('错了')
            continue
        else:
            l.append(g)
    y=sorted(l)
    v=l[2:-2]
    for g in v:
        er+=g
    return (er/3)*p
print(a(p))




