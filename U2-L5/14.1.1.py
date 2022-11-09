class People:
    def talk(self):
        print('Ahhhh')


class Infrant(People):
    def talk(self):
        self.__a=1
s1 = Infrant
s1.talk(7)