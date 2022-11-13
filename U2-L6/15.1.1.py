class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()
'''
B --> A --> C --> A --> D
'''
