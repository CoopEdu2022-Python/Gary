import random


class Player:
    def __init__(self, points):
        self.points = points

    def punch(self):
        return random.choice([10, 5, 2])

    def challenge(self):
        return random.choice['yes', 'no']


class Computer(Player):
    def __init__(self, points):
        super().__init__(points)

    def punch(self):
        super().punch()


class Fraud:
    def lie(self):
        return random.choice(['lose', 'tie'])


player1scroe = 0
computer1scroe = 0
player1 = Player(player1scroe)
computer1 = Computer(computer1scroe)
fraud1 = Fraud()


def game():
    global player1scroe
    global computer1scroe
    a = 0
    b = 0
    if player1.punch() > computer1.punch():

        a += 1
    elif player1.punch() < computer1.punch():
        b += 1
    if player1.challenge() == 'yes':
        if fraud1.lie() == 'tie':
            a = 0
        else:
            a = -2
    player1scroe = player1scroe + a
    computer1scroe = computer1scroe + b
