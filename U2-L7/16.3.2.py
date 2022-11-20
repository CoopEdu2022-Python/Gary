import random

message = str()


class Judge:
    def closeeyes(self):
        global message
        message = 'close'


class Mafia:
    def __init__(self, code):
        self.code = code

    def decide(self):
        return random.randint(1, 10)


class good:
    def __init__(self, code):
        self.code = code

    def decide(self):
        return random.randint(1, 10)


allgood = []
for i in range(6):
    allgood.append(good(i))
allbad = []
for i in range(6, 11):
    allbad.append(Mafia(i))

while allbad != 0 or allgood != 0:
    die = []
    for g in allbad:
        die.append(g.decide())
    die.sort()
    if die[0] == die[1] or die[1] == die[2]:
        if die[1] >= 5:
            allgood.pop(die[1])
        if die[1] <= 9:
            allbad.pop(die[1])
        die.clear()
    else:
        if die[1] >= 5:
            allgood.pop(die[2])
        if die[1] <= 9:
            allbad.pop(die[2])
    all = allbad + allgood
    for h in all:
        die.append(h.decide())
    die.sort()
    for x,y in enumerate(set(die)):
        pass