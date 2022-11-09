class A:
    def test(self):
        print(1)


class B(A):
    def test(self):
        print(2)


class C(B):
    # write code here
    def __init__(self):
        super(A,self).test()