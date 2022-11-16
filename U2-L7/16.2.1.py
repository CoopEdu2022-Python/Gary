import random


class Dealer:
    def __init__(self):
        self.number = self.set_number()

    def set_number(self):
        self.number = random.randint(1, 100)
        return self.number

    def hint(self, n):
        if self.number > n:
            return "Too low"
        elif self.number < n:
            return "Too high"
        else:
            return "Correct"

    def award(self, rounds):
        return 10 - rounds

class Player:
    def __init__(self, name):