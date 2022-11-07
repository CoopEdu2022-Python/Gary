def max_sec_average(l, n):
    a = len(l) - n
    b = []
    v = []
    for i in range(a):
        b.append(l[i:i + n])
        b.append(l[i + n:i:-1])
    for g in b:
        u = 0
        for y in g:
            u += y
        v.append(u)
    return max(v)/n


print(max_sec_average([1, 12, -5, -6, 50, 3], 4))
