class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print("B")


class C(A):
    def __init__(self):
        super(C, self).__init__()
        print("C")


class D(B, C):
    pass


d = D()
'''

B --> A --> C --> A --> D
'''