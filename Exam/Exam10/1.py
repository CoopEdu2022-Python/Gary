def uncommon(a, b):
    n = 0
    if a == b:
        return -1
    if len(a) < len(b):

        for i in a:
            if a not in b:
                n += 1

    return n


print(uncommon('hfmezmg', 'kgfqfeenshfw'))
