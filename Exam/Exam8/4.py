import random


class Player:
    def __init__(self, points):
        self.points = points

    def punch(self):
        return random.choice([10, 5, 2])


class Computer(Player):
    def __init__(self, points):
        super().__init__(points)

    def punch(self):
        super().punch()
player1scroe = 0
computer1scroe = 0
player1=Player(player1scroe)
computer1 = Computer(computer1scroe)

def game():
    global player1scroe
    global computer1scroe
    if player1.punch()>computer1.punch():

        player1scroe +=1
    elif player1.punch()<computer1.punch():
        computer1scroe+=1
