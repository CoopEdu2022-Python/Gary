def gcd_pro_max_2(*n):
    h = sorted(n)
    a=0
    for i,p in enumerate(h):
        if h[i]//h[i+1]==1:
            a+=1

        else:
            h[i] = h[i] % h[i+1]





