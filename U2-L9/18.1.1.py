class A:
    nums = 0

    def __init__(self):
        self.nums = 0

    @classmethod
    def test1(cls):
        dir_A = []
        for i in dir(A):
            if not i.startswith('__') and not i.endswith('__'):
                dir_A.append(i)
        return dir_A

    @classmethod
    def test2(cls):
        dir_cls = []
        for i in dir(cls):
            if not i.startswith('__') and not i.endswith('__'):
                dir_cls.append(i)
        return dir_cls

    def test3(self):
        dir_self = []
        for i in dir(self):
            if not i.startswith('__') and not i.endswith('__'):
                dir_self.append(i)
        return dir_self


a = A()
print(a.test1())
print(a.test2())
print(a.test3())