def gcd_pro_max_2(*n):
    h = sorted(n)
    h = h[::-1]
    while len(set(h))>1:
        h=sorted(n)
        h = h[::-1]
        for i in range(len(n) - 1):
            if h[i] % h[i + 1] == 0:
                h[i] = h[i + 1]
            else:
                h[i] = h[i] % h[i + 1]
    return h[0]


def gcd_pro_max_1(*n):
    h = sorted(n)
    h = h[::-1]
    if len(set(h))==1:
        return h[0]

    for i in range(len(n) - 1):
        if h[i] % h[i + 1] == 0:
            h[i] = h[i + 1]
        else:
            h[i] = h[i] % h[i + 1]
        return gcd_pro_max_1(*h)

print( gcd_pro_max_2(2, 4, 6, 8, 10))
