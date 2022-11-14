import random


class Fish:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(1, 10)
        self.speed = 1

    def judge(self, o):
        if o > 10:
            return 9
        if o < 10:
            return 1
        return o


class Bigfish(Fish):
    def __init__(self):
        super().__init__()
        self.hp = 100

    def move(self):
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)
        self.x = self.x + x
        self.x = self.judge(self.x)
        self.y = self.y + y
        self.y = self.judge(self.y)
        self.hp = self.hp - (abs(x) + abs(y))

    def eat(self):
        self.hp = self.hp + 20
        if self.hp > 100:
            self.hp = 100


class SmallFish(Fish):
    def move(self):
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)
        a = random.randint(0, 1)
        if a == 0:
            self.x = self.x + x
            self.x = self.judge(self.x)
        else:
            self.y = self.y + y
            self.y = self.judge(self.y)


big_fish = Bigfish()
small_finshes = list()
for i in range(10):
    small_finshes.append(SmallFish())
while big_fish.hp > 0 and small_finshes != []:
    big_fish.move()
    eaten_fishes = []
    for i, small_finsh in enumerate(small_finshes):
        small_finsh.move()
        if (big_fish.x, big_fish.y) == (small_finsh.x, small_finsh.y):
            big_fish.eat()
            eaten_fishes.append(i)
    a=[]
    for i in eaten_fishes:
        a.append(small_finshes[i])
    for i in a:
        small_finshes.remove(i)

    if big_fish.hp <= 0:
        print('大鱼死了')
    if small_finshes == []:
        print('吃完了')
