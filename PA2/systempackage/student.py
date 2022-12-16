import os


class Student:
    courselist = []
    for i in os.listdir():
        if i[0:6] == 'course:':
            courselist.append(i[5:])

    def __init__(self, name):
        self.name = name

    @staticmethod
    def sync(name):
        with open('student:' + name + '.txt', 'r') as f:
            all = f.readlines()
            type = []
            Selected_Credit = []
            credit = all[1][8:-1]
            lesson = all[2][8:-1]
            for i in range(len(lesson)):
                for i in os.listdir():
                    if i[8:-4] in lesson:
                        with open(i, 'r') as f:
                            a = f.readlines()
                            type.append(a[2][14:-1])
                            Selected_Credit.append(a[3][8:-1])
            return type, Selected_Credit, credit, lesson

    @staticmethod
    def createstudent(name, credit, lesson, password):
        with open('student:' + name + '.txt', 'w') as student_info:
            student_info.write('Name:' + name + '\n')
            student_info.write('Required_Credit:' + str(credit))
            student_info.write('lessons:' + str(lesson))
            student_info.write('password:' + str(password))
        with open('course_select_report:' + name + '.txt', 'w') as select_report:
            type, Selected_Credit, _credit, _lesson = Student.sync(name)

            select_report.write('Name:' + name + '\n')
            select_report.write('Required_Credit:' + str(_credit))
            select_report.write('Selected_Credit:' + str(Selected_Credit))
            select_report.write('type:' + str(type))
            select_report.write('lessons:' + str(_lesson))

    def update(self):
        type, Selected_Credit, credit, lesson = Student.sync(self.name)
        with open('course_select_report:' + self.name + '.txt', 'w') as select_report:
            select_report.write('Name:' + self.name + '\n')
            select_report.write('Required_Credit:' + str(credit))
            select_report.write('Selected_Credit:' + str(Selected_Credit))
            select_report.write('type:' + str(type))
            select_report.write('lessons:' + str(lesson))

    def add_course(self, course):

        if course in self.courselist:

            course_info = open('course:' + course + '.txt', 'r+')
            all = course_info.readlines()

            student_list = all[5][14:-1].split(',')[0:-1]

            student_num = all[4][16:-1]
            course_credit = all[3][8:-1]
            course_type = all[2][12:-1]

            if self.name in student_list:
                print('你已经选过这门课了')
            elif len(student_list) >= int(student_num):
                print('这门课已经满了')
            else:
                student_list.append(self.name)
                all[5] = ('Student list: {}'.format(''.join(str(i) + ',' for i in student_list)))
                course_info.close()
                course_info = open('course:' + course + '.txt', 'w')
                course_info.writelines(all)
                print('选课成功')
                course_info.close()
                self.update()
                with open('course_select_report:' + self.name + '.txt', 'r') as course_select_report:
                    all = course_select_report.readlines()
                    if 'required' not in list(all[3][5:-1]):
                        print('你没有选必修课')
                    if 'optional' not in list(all[3][5:-1]):
                        print('你没有选选修课')
                    if int(all[1][16:-1]) < int(all[2][16:-1]):
                        print('你的学分不够')

            course_info.close()





        else:
            print('没有这节课')

    def drop_course(self, course):

        if course in self.courselist:
            courseinfor = open('course:' + course + '.txt', 'r+')
            all = courseinfor.readlines()

            studentlist = all[5][14:-1].split(',')[0:-1]

            if self.name in studentlist:
                studentlist.remove(self.name)
                all[5] = ('Student list: {}'.format(''.join(str(i) + ',' for i in studentlist)))
                courseinfor.close()
                courseinfor = open('course:' + course + '.txt', 'w')
                courseinfor.writelines(all)
                print('退课成功')
                self.update()
            else:
                print('你没有选这门课')
            courseinfor.close()
        else:
            print('没有这节课')

    def seestucourse(self, course):

        if course in self.courselist:
            courseinfor = open('course:' + course + '.txt', 'r')
            print(courseinfor.read())
            courseinfor.close()
        else:
            print('没有这节课')

    @staticmethod
    def set_credit(name, credit):
        student_info = open('student:' + name + '.txt', 'r+')
        all = student_info.readlines()
        all[1] = 'Credit:' + str(credit)
        student_info.close()
        student_info = open('student:' + name + '.txt', 'w')
        student_info.writelines(all)
        student_info.close()
        print('学分设置成功')
