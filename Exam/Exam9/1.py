def a():
    return 1


def b():
    try:
        print(a())
        return True
    finally:
        print(2)
b()
"""
Finally的运行原理应该是如果程序种含有Finally语句,Finally代替原来的return只有Finally运行之后才会退出函数
"""