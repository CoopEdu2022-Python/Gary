def hamming_distance(x: int, y: int) -> int:
    global x1
    a=bin(x)[2:]
    b=bin(y)[2:]
    if len(a) <32:
        a='0'*(32-len(a))+a
    if len(b)<32:
        b='0'*(32-len(b))+b
    x1=0
    x2=0

    for x,y in enumerate(a):
        if y =='1':
            if x>x1:
                x1=x
    for e,r in enumerate(b):
        if r == '1':
            if e > x2:
                x2 = e
    return abs(x1-x2)


