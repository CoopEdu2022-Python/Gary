def perms(l):
    a = []
    for i in l:
        for g in l:
            for h in l:
                for k in l:
                    for y in l:
                        e = [i, g, h, k, y]
                        r = []
                        for q in e:
                            if q not in r:
                                r.append(q)
                        if len(r) == 5:
                            a.append(tuple(r))
    b = []
    for d in a:
        if d not in b:
            b.append(d)
    return b,len(b)


print(perms([1, 2, 3, 4, 5]))
