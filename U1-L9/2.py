def taijie(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n == 2:
        return 2
    return taijie(n-1)+taijie(n-2)
print(taijie(2))