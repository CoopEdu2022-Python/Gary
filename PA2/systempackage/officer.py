import os


class officer:
    def __init__(self, name):
        self.name = name

    def create_student(self, name, credit, lesson, password):
        return name, credit, lesson, password

    def set_credit(self, name, credit):
        return name, credit

    def see_profile(self, name):
        info = open('student_' + name + '.txt', 'r')
        all = info.read()
        print(all)
        info.close()

    def create_course(self, name, student_list, teacher, course_type, credit, student_num):
        return name, student_list, teacher, course_type, credit, student_num

    def change_course(self, name):
        os.system('course_' + name + '.txt')

    def see_course(self, name):
        os.startfile('course_' + name + '.txt', 'print')

    def see_stu_course(self, name):
        os.startfile('course_select_report_' + name + '.txt', 'print')

    def create_officer(self, name, password):
        student_info = open('officer_' + name + '.txt', 'w')
        student_info.write('Name:' + name + '\n')

        student_info.write('password:' + str(password))
        student_info.close()
