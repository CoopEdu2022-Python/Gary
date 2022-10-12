text = 'edcw cef 234 ?//'


def U(text):
    words = 0
    num = 0
    space = 0
    symbol = 0
    other = 0
    for i in text:
        if i.isalpha():
            words += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            space += 1
        elif i.isidentifier():
            symbol += 1
        else:
            other += 1
    p = ('words:', words, 'num:', num, 'space:', space, 'symbol:', symbol, 'other:', other)
    print(tuple(p))
