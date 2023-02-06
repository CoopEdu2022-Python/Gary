def funnumber(a):
    w = a * 2
    print(w)
    e = [i for i in str(a)]
    g = 'yes'
    for i in str(w):
        if i in e:
            try:
                e.remove(i)
            except:
                pass

        else:
            g = 'no'
    if len(e)!=0:
        g='no'
    print(g)
funnumber(1234567899)