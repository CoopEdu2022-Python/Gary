def MAX(s):
    a = []
    for i in s:
        a.append(i)
    a.sort()
    b = a[-1] + 1
    a.remove(a[-1])
    a.append(b)
    return a


print(MAX([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
