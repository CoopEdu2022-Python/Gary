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


scores = 0
round = 0


dealer = Dealer()
player = Player(scores)
def game(dealer,player):

    a = dealer.set_number()

    b = player.guess_number()
    if dealer.hint(b):
        global scores
        scores = dealer.award(rounds)


while scores >= -10:
    round = round + 1
    game(round, scores)
    print(scores)
