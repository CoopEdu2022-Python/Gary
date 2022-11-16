import random


class Dealer:
    def __init__(self):
        self.number = self.set_number()

    def set_number(self):
        self.number = random.randint(1, 100)
        return self.number

    def hint(self, n):
        if self.number > n:
            print("Too low")
        elif self.number < n:
            print('Too high')
        else:
            print('correct')
            return True

    def award(self, rounds):
        return 10 - rounds


class Player:
    def __init__(self, point):
        self.point = point

    def guess_number(self):
        return random.randint(0, 100)


def game(rounds, v):
    dealer = Dealer()
    a = dealer.set_number()
    player = Player(v)
    b = player.guess_number()
    if dealer.hint(b):
        dealer.award(rounds)


game(1, 100)

#2
rounds = 0
while True:
    rounds +=1
