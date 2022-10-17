text = '123321'


def a(text):
    return text == text[::-1]


print(a(text))
