import os


class Student:
    courselist = []
    for i in os.listdir():
        if i[0:6] == 'course:':
            courselist.append(i[5:])

    def __init__(self, name):
        self.name = name

    @staticmethod
    def createstudent(name, credit, lesson, password):
        with open('student:' + name + '.txt', 'w') as student_info:
            student_info.write('Name:' + name + '\n')
            student_info.write('Credit:' + str(credit))
            student_info.write('lessons:' + str(lesson))
            student_info.write('password:' + str(password))
        with open('course_select_report:' + name + '.txt', 'w') as select_report:
            select_report.write('Name:' + name + '\n')
            select_report.write('Required_Credit:' + str(credit))
            select_report.write('Selected_Credit:' + str(0))
            select_report.write('lessons:' + str(lesson))



    def addcourse(self, course):

        if course in self.courselist:

            courseinfor = open('course:' + course + '.txt', 'r+')
            all = courseinfor.readlines()

            studentlist = all[5][14:-1].split(',')[0:-1]

            studentnum = all[4][16:-1]
            course_credit = all[3][8:-1]
            course_type = all[2][12:-1]


            if self.name in studentlist:
                print('你已经选过这门课了')
            elif len(studentlist) >= int(studentnum):
                print('这门课已经满了')
            else:
                studentlist.append(self.name)
                all[5] = ('Student list: {}'.format(''.join(str(i) + ',' for i in studentlist)))
                courseinfor.close()
                courseinfor = open('course:' + course + '.txt', 'w')
                courseinfor.writelines(all)
                print('选课成功')

            courseinfor.close()




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
