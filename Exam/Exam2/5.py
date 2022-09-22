
for g in range(1,1001):
    q=0
    for i in range(1, g):
        if g % i == 0:
            q=q+i

    if q == g:
        print(q)

