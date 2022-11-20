def changelist(list):
    c = len(list) / 2
    a = list[:int(c)]
    b = list[int(c):]
    g = []
    for i in range(int(c)):
        g.append(a[i])
        g.append(b[i])
    return g


print(changelist([2, 5, 1, 3, 4, 7]))
