import os


class officer:
    def __init__(self, name):
        self.name = name

    def create_student(self, name, credit, lesson, password):
        return name, credit, lesson, password

    def set_credit(self, name, credit):
        return name, credit

    def see_profile(self, name):
        return name

    def create_course(self, name, student_list, teacher, course_type, credit, student_num):
        return name, student_list, teacher, course_type, credit, student_num

    def change_course(self, name):
        return name

    def see_course(self, name):
        return name

    def see_stu_course(self, name):
        return name

    def create_officer(self, name, password):
        return name, password
