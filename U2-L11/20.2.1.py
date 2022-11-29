class B:
    m = 100
    n = 99

    def __init__(self):
        self.m = 98
        self.n = 97

    def __del__(self):
        pass

    def __func1(self):
        self.m += 94
        self.n += 93

    def func2(self):
        self.m -= 92
        self.n -= 91

    @classmethod
    def func3(cls):
        cls.m += 90
        cls.n += 89

    def func4(cls, self):
        cls.m -= 88
        cls.n -= 87
        self.m -= 86
        self.n -= 85

    @staticmethod
    def func5():
        print(84)

    def func6(cls):
        cls.m += 83
        cls.n += 82
"""
Builtin method（2），Static method（1）
Class attribute（2），Class method（1）
Instance Attribute（2），Instance method（2）

print(B.m, B.n)
100 99调用类属性

b = B()
b.__func1()
print(b.m, b.n)

报错因为是私有方法

b = B()
b.func2()
print(B().m, B().n)

98 97调用实例属性，打印的是B()的属性，不是修改过的因为修改的是b的属性

B.func3()
print(B.m, B.n)

190 198修改的类属性，因为是类方法

func5()

静态方法需要类名+方法或者实例名+方法调用，报错
"""
b = B()
b.func4(b)
print(b.m, b.n, B.m, B.n)
"""
-76 -76 190 198🤔
"""
b = B()
b.func6()
print(B.m, B.n)
"""
100 99打印类属性，但是方法作用在了实例b上，所以类属性没有修改
"""