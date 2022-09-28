a = int(input('?'))


def n(a):
    b = 1
    c = 0
    while b <= a:
        g = int(input('?'))
        if 100 < a < 0:
            print('用户输入错误')
            continue
        else:
            b+=1
            c+=g
    return c/a
print(n(a))

