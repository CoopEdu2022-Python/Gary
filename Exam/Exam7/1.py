def gcd_pro_max_2(*n):
    h = sorted(n)
    a=0
    for i,p in enumerate(h):
        if i ==0:
            a=a+1
        elif h[i+1] == p:
            a=a+1
        else:
            h[i] = h
    if a == len(a)+1:
        return True





