class Animal:
    def __init__(self, health):
        self.health = health
        if self.health > 100:
            self.health = 100


class Manager:
    def feed(self, health):
        health += 20
        return health

    def perform(self, health):
        health -= 20
        return health

    def inspect(self, value):
        if 0 <= value <= 100:
            return value


class Keeper(Manager):
    def __init__(self, performance, health):
        self.performance = performance
        if health < 80:
            self.performance -= 20

    def perform(self, health):
        print('没有这个方法')

    def inspect(self, value):
        print('没有这个方法')


class Trainer(Manager):
    def __init__(self, performance, health):
        self.performance = performance
        if health < 80:
            self.performance -= 20

    def feed(self, health):
        print('没有这个方法')

    def inspect(self, value):
        print('没有这个方法')

def everyday():
    dog = Animal(100)
    perzon = Manager()

    dog.health = perzon.feed(dog.health)

    perzon1 = Keeper(100,dog.health)

    perzon2 = Trainer(100,dog.health)


