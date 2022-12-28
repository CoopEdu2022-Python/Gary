import os


class Controller:
    def __init__(self, name):
        self.student_list = []
        self.officer_list = []
        self.course_list = []
        self.name = name
        for i in os.listdir():
            if i.startswith('student_'):
                self.student_list.append(i[8:-4])
            elif i.startswith('officer_'):
                self.officer_list.append(i[8:-4])
            elif i.startswith('course_'):
                self.course_list.append(i[7:-4])

    def create_course(self, name, student_list, teacher, course_type, credit, student_num):

        if name not in self.course_list:
            with open('course_' + name + '.txt', 'w') as course_info:

                course_info.write('Course name: ' + name + '\n')
                course_info.write('Teacher: ' + teacher + '\n')
                course_info.write('Course type: ' + course_type + '\n')
                course_info.write('Credit: ' + str(credit) + '\n')
                course_info.write('Student number: ' + str(student_num) + '\n')
                student_list = ''.join(str(i) + ',' for i in student_list)
                course_info.write('Student list: {}\n'.format(student_list))

                print('课程创建成功')
                return True

        else:
            print('名称已经用过')
            return False

    def see_profile(self, name):
        info = open('student_' + name + '.txt', 'r')
        all = info.read()
        print(all)
        info.close()

    def change_course(self, name):
        os.system('course_' + name + '.txt')

    def see_course(self, name):
        os.startfile('course_' + name + '.txt', 'print')

    def create_officer(self, name, password):
        student_info = open('officer_' + name + '.txt', 'w')
        student_info.write('Name:' + name + '\n')

        student_info.write('password:' + str(password))
        student_info.close()

    def sync(self, name):
        with open('student_' + name + '.txt', 'r') as f:
            all = f.readlines()
            type = []
            Selected_Credit = []
            credit = all[1][16:-1]
            lesson = all[2][8:-1].split(',')
            for _ in range(len(lesson)):
                for i in os.listdir():
                    if i[8:-4] in lesson:
                        with open(i, 'r') as course_file:
                            a = course_file.readlines()
                            type.append(a[2][13:-1])
                            Selected_Credit.append(int(a[3][8:-1]))
            return ','.join(type), sum(Selected_Credit), credit, ','.join(lesson)

    def update(self, name):
        type, Selected_Credit, credit, lesson = self.sync(name)
        with open('course_select_report_' + name + '.txt', 'w') as select_report:
            select_report.write('Name:' + name + '\n')
            select_report.write('Required_Credit:' + str(credit) + '\n')
            select_report.write('Selected_Credit:' + str(Selected_Credit) + '\n')
            select_report.write('type:' + str(type) + '\n')
            select_report.write('lessons:' + str(lesson) + '\n')

    def create_student(self, name, credit, lesson, password):
        with open('student_' + name + '.txt', 'w') as student_info:
            student_info.write('Name:' + name + '\n')
            student_info.write('Required_Credit:' + str(credit) + '\n')
            student_info.write('lessons:' + str(lesson) + '\n')
            student_info.write('password:' + str(password) + '\n')
        self.update(name)

    def add_course(self, course):

        if course in self.course_list:

            with open('course_' + course + '.txt', 'r+') as course_info:
                file_all = course_info.readlines()

                student_list = file_all[5][14:-1].split(',')

                student_num = file_all[4][16:-1]

                course_info.close()
            if self.name in student_list:
                print('你已经选过这门课了')
            elif len(student_list) >= int(student_num):
                print('这门课已经满了')
            else:
                student_list.append(self.name)
                file_all[5] = ('Student list: {}'.format(','.join(student_list)))
                course_info.close()
                course_info = open('course:' + course + '.txt', 'w')
                course_info.writelines(file_all)
                print('选课成功')
                course_info.close()
                self.update(self.name)

                with open('course_select_report:' + self.name + '.txt', 'r') as course_select_report:
                    file_all = course_select_report.readlines()
                    if 'required' not in list(file_all[3][5:-1]):
                        print('你没有选必修课')
                    if 'optional' not in list(file_all[3][5:-1]):
                        print('你没有选选修课')
                    if int(file_all[1][16:-1]) < int(file_all[2][16:-1]):
                        print('你的学分不够')
        else:
            print('没有这节课')

    def drop_course(self, course):

        if course in self.course_list:
            course_infor = open('course:' + course + '.txt', 'r+')
            file_all = course_infor.readlines()

            student_list = file_all[5][14:-1].split(',')
            course_infor.close()
            if self.name in student_list:
                student_list.remove(self.name)
                file_all[5] = ('Student list: {}'.format(','.join(student_list)))
                course_infor.close()
                course_infor = open('course:' + course + '.txt', 'w')
                course_infor.writelines(file_all)
                print('退课成功')
                self.update(self.name)
            else:
                print('你没有选这门课')

        else:
            print('没有这节课')

    def see_stu_course(self, course):

        if course in self.course_list:
            course_infor = open('course:' + course + '.txt', 'r')
            print(course_infor.read())
            course_infor.close()
        else:
            print('没有这节课')

    def set_credit(self, name, credit):
        student_info = open('student:' + name + '.txt', 'r+')
        file_all = student_info.readlines()
        file_all[1] = 'Credit:' + str(credit) + '\n'
        student_info.close()
        student_info = open('student:' + name + '.txt', 'w')
        student_info.writelines(file_all)
        student_info.close()
        self.update(name)
        print('学分设置成功')
