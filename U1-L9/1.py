def hs(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    return 2 * hs(n - 1) + 1


print(hs(2))
