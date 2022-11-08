class Person:
    def __init__(self, name):
        self.__name = name

    def changprivate(self, new_name):
        if len(new_name) < 10:
            self.__name = new_name
        print(self.__name)



person1 = Person('gary')

person1.changprivate('zhanghjhgjhg')
