def num(a):
    if a == 1:
        return '1 * 1 = 1 \n1'
    elif a == 2:
        return '2 * 1 = 2 2 * 2 = 4 \n3'
    elif a == 3:
        return '3 * 1 = 3 3 * 2 = 6 3 * 3 = 9 \n6'
    elif a == 4:
        return '4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16 \n10'
    elif a == 5:
        return '5 * 1 = 5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25 \n15'
    elif a == 6:
        return '6 * 1 = 6 6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36 \n21'
    elif a == 7:
        return '7 * 1 = 7 7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49 \n28'
    elif a == 8:
        return '8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 \n36'
    elif a == 9:
        return '9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81 \n45'
    else:
        return '!'


a = int(input('?'))
print(num(a))
