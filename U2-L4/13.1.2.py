class Exam:
    def __init__(self,id,start_time,end_time,points):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.points = points
class Test(Exam):
    def change(self):
        del self.start_time
        del self.end_time
        self.__points = 10


