import math


class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, xy1, xy2):
        self.__xy1 = str(xy1).split(',')
        self.__xy2 = str(xy2).split(',')

    def get_len(self):
        final = math.sqrt(
            ((int(self.__xy1[0])) - int(self.__xy2[0])) ** 2 + ((int(self.__xy1[1])) - int(self.__xy2[1])) ** 2)
        print(final)


s = Segment('2,5', '3,5')
s.get_len()
