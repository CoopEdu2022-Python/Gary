class Animal:
    def __init__(self, health):
        self.health = health
        if self.health > 100:
            self.health = 100


class Manager:
    def __init__(self, health):
        self.animal = Animal(health)
        self.animal = self.animal.health

    def feed(self):
        self.animal.health += 20


    def perform(self):
        self.animal.health -= 10

    def inspect(self, value):
        if 0 <= value <= 100:
            return value



class Keeper(Manager):
    def __init__(self, performance):
        super().__init__(health)
        self.performance = performance
        if self.health < 80:
            self.performance -= 20

    def perform(self):
        print('没有这个方法')

    def inspect(self, value):
        print('没有这个方法')


class Trainer(Manager):
    def __init__(self, performance, health):
        super().__init__(health)
        self.performance = performance
        if self.health < 80:
            self.performance -= 20

    def feed(self):
        print('没有这个方法')

    def inspect(self, value):
        print('没有这个方法')
def everyday():
    dog = Animal(100)
    manager = Manager(100)
    keeper = Keeper(100, 100)
    trainer = Trainer(100, 100)
    manager.feed()
    keeper.perform()
    trainer.perform()





