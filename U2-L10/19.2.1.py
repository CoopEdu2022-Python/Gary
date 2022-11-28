import random

class AB(Exception):
    pass


def startend(a,b):

    a = input('start: ')
    b = input('end: ')
    a = int(a)
    b = int(b)
    if a > b:
        raise AB()
    c = random.randint(a, b)
    return c


try:

    print(startend(1, 10))
except ValueError:
    print('请输入整数')
except AB():


    print('a不能大于b')
