class Student:
    def __init__(self, name=str(), id=str()):
        self.name = str(name)
        self.id = str(id)
        self.cause = list()

    def get_course(self):
        return self.cause

    def __len__(self):
        return len(self.cause)

    def __str__(self):
        return 'name:{} id:{}'.format(self.name, self.id)


Student_1 = Student('z', '233')
print(Student_1)

