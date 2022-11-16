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
            return 'low'
        elif self.number < n:
            print('Too high')
            return 'high'
        else:
            print('correct')
            return True

    def award(self, rounds):
        return 10 - rounds


class Player:
    def __init__(self, point):
        self.point = point


    def guess_number(self,n1,n2):
        return random.randint(n1, n2+1)


scores = 0
round = 0


def game(rounds, v):
    n1 = 0
    n2 = 100
    dealer = Dealer()
    a = dealer.set_number()
    player = Player(v)
    b = player.guess_number(n1,n2)
    if dealer.hint(b)=='low':
        n1+=1
        n2+=1
    elif dealer.hint(b) == 'high':
        n1-=1
        n2-=1


    elif dealer.hint(b):
        scores = dealer.award(rounds)
        global scores

game(1,100)

