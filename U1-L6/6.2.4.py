def g(n):
    a = 0
    if 'IV' in n:
        a = a + 4
        n = n.replace('IV', '')
    if 'IX' in n:
        a = a + 9
        n = n.replace('IX', '')
    if 'XL' in n:
        a = a + 40
        n = n.replace('XL', '')
    if 'XC' in n:
        a = a + 90
        n = n.replace('XC', '')
    if 'CD' in n:
        a = a + 400
        n = n.replace('CD', '')
    if 'CM' in n:
        a = a + 900
        n = n.replace('CM', '')

    for i in n:

        if i == 'I':
            a = a + 1
        elif i == 'V':
            a = a + 5
        elif i == 'X':
            a = a + 10
        elif i == 'L':
            a = a + 50
        elif i == 'C':
            a = a + 100
        elif i == 'D':
            a = a + 500
        elif i == 'M':
            a = a + 1000

    return a


print(g('LVIII'))
