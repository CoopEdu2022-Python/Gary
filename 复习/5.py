class Student:
    def __init__(self):
        self.name = 'student'
        self.score = 0

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


student_1 = Student()
print(student_1.name)
print(student_1.score)
student_1.print_score()