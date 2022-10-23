def Y(n):
    a = 0
    for i in str(n):
        a = a + int(i) ** 2
    if a == 1:
        return True
    else:
        return False


print(Y(19))
