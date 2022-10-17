text = 'edcw cef 234 ?//'


def U(text):
    words = 0
    num = 0
    space = 0

    other = 0
    for i in text:
        if i.isalpha():
            words += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            space += 1

        else:
            other += 1
    p = ('words:', words, 'num:', num, 'space:', space, 'other:', other)
    print(tuple(p))
