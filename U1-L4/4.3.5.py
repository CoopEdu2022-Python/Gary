def h(num):
    a = ''
    b = ''
    c = ''

    d = ''
    if num % 2 == 1:
        num = num // 2 + 1
        for i in range(1, 2 * num, 2):
            a = '*' * i
            d += (' ' * (2 * num - 1 - i))

            
        for n in range(2 * num - 3, 0, -2):
            c = '*' * n


a = int(input('?'))
print(a)
