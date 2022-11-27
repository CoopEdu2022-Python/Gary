def triangle(a, b, c):
    IllegalArgumentException = Exception('不能组成三角形')

    if max(a, b, c) > a + b + c - max(a, b, c):
        return True
    else:
        raise IllegalArgumentException
try:
    triangle(1, 2, 3)
except Exception:
    print('a, b, c 不能构成三角形')

