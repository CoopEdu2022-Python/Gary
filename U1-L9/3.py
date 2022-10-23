def r(n):
    n=str(n)
    if n == 1:
        return 1
    elif n == 0:
        return 0

    return r(n[1:])+n[0]

print(r('12345'))