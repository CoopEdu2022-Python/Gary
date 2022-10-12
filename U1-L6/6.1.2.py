text = '123321'


def H(text):
    a = 0
    if len(text) % 2 == 0:

        a = text[0:(len(text) // 2)]

    else:
        a = text[0:(len(text) // 2) + 1]
    b = []
    c = ''
    if len(text) % 2 == 0:
        for i in range(1, (len(text) // 2) + 2):
            b.append(str(i))
    else:
        for i in range(1, (len(text) // 2) + 1):
            b.append(str(i))
    d = c.join(b)
    if a == d:
        if text == text[::-1]:
            print('是的')
        else:
            print('不是')
    else:
        print('不是')
