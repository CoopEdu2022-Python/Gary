'''定义水果类 Fruit，包含类属性品种 variety
定义 5 个品种的水果类，继承自 Fruit，包含类属性数量 nums
在主程序中分别为 5 种水果创建若干实例，打印水果的品种数以及各自品种的数量'''


class Fruit:
    varirty = 0



class Graps(Fruit):
    nums = 0
    Fruit.varirty += 1

    def __init__(self):
        Graps.nums += 1



class Orange(Fruit):
    nums = 0
    Fruit.varirty += 1

    def __init__(self):
        Orange.nums += 1


class Banana(Fruit):
    nums = 0
    Fruit.varirty += 1

    def __init__(self):
        Banana.nums += 1


class Apple(Fruit):
    nums = 0
    Fruit.varirty += 1

    def __init__(self):
        Apple.nums += 1


class Pear(Fruit):
    nums = 0
    Fruit.varirty += 1

    def __init__(self):
        Pear.nums += 1


class Mango(Fruit):
    nums = 0
    Fruit.varirty += 1

    def __init__(self):
        Mango.nums += 1


Fruit1 = Fruit()
Graps1 = Graps()
Graps2 = Graps()
Orange1 = Orange()
Orange2 = Orange()
Orange3 = Orange()
Banana1 = Banana()
Banana2 = Banana()
Banana3 = Banana()
Banana4 = Banana()
Apple1 = Apple()
Apple2 = Apple()
Apple3 = Apple()
Apple4 = Apple()
Apple5 = Apple()
Pear1 = Pear()
Pear2 = Pear()
Pear3 = Pear()
Pear4 = Pear()
Pear5 = Pear()
Pear6 = Pear()
Mango1 = Mango()
Mango2 = Mango()
Mango3 = Mango()

print(Fruit.varirty)