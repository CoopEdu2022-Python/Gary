class A:
    def __init__(self):
        self.__a = 1

    def change(self,value):
        self.__a = value
class B(A):
    def __init__(self):
        self.__b = 2
    def changevalue(self,value1):
        super().change(value=value1)




b1 = B()
b1.changevalue('a')
