text1 = 'dsvfgbnhgfes'
text2 = 'gtdr'


def H(text1, text2):
    v = ''

    for a in text1:
        if a in text2:
            v = text1.replace(a, '')
    return v
print(H(text1, text2))