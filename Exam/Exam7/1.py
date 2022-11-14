def gcd_pro_max_2(*n):
    h = sorted(n)
    h = h[::-1]
    while h[0] != h[-1]:

        for i in range(len(n)-1):
            if h[i]%h[i+1]==0:
                h[i]=h[i+1]
            else:
                h[i] = h[i] - h[i+1]
    return h[0]
def gcd_pro_max_1(*n):
    h = sorted(n)
    h = h[::-1]
    if h[0]!=h[-1]:
        return h[0]

    for i in range(len(n)-1):
        if h[i]%h[i+1]==0:
            h[i]=h[i+1]
        else:
            h[i] = h[i] - h[i+1]
            return gcd_pro_max_1(*h)

        return h[0]




