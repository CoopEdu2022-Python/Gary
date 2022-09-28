a = int(input('?'))


def n(a):
    b = 1
    c = 0
    l = []

    while b <= a:
        g = int(input('?'))
        if 100 < a < 0:
            print('用户输入错误')
            continue
        else:
            l.append(g)
            b += 1
            c += g
            u = tuple(l)
    return u


t = n(a)
c = 0
for i in t:
    c += int(i)
print(c / a)
g = list(t)
g[0] = 1
c = 0
for i in g:
    c += int(i)
print(c / a)
