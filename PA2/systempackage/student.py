


class Student:

    def __init__(self, name):
        self.name = name

    def add_course(self, course):
        return self.name, course

    def drop_course(self, course):
        return self.name, course

    def see_stu_course(self, course):
        return self.name, course
