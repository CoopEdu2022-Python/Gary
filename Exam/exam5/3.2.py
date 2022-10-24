def y(n):
    a = bin(n)
    u=a[2:]
    c=str(u)
    if len(c) != 32:
        c = '0' * (32 - len(c))+c
    o=c[::-1]
    h='0b'+o
    print(c)
    print(o)
    return int(h,2)

print(y(43261596))

