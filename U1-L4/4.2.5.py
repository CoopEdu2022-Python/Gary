def h(num):
    a = ''
    b = ''
    c = ''

    d = ''
    if num % 2 == 1:
        num = num // 2 + 1
        for i in range(1, 2 * num, 2):
            a = '*' * i
            print(a.center(2 * num - 1))
        for n in range(2 * num - 3, 0, -2):
            c = '*' * n
            print(c.center(2 * num - 1))
a = int(input('?'))
h(a)