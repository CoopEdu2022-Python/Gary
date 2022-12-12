import os


class Student:
    def __init__(self, name):
        self.name = name
        self.courselist = []
        for i in os.listdir():
            if i[0:6] == 'course:':
                self.courselist.append(i[5:])

    @staticmethod
    def createstudent(name, credit, lesson, password):
        studentinfo = open('student:' + name + '.txt', 'w')
        studentinfo.write('Name:' + name + '\n')
        studentinfo.write('Credit:' + str(credit))
        studentinfo.write('lessons:' + str(lesson))
        studentinfo.write('password:' + str(password))

    def addcourse(self, course):

        if course in self.courselist:

            courseinfor = open('course:' + course + '.txt', 'r+')
            all = courseinfor.readlines()

            studentlist = all[5][14:-1].split(',')[0:-1]

            studentnum = all[4][16:-1]

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

    def dropcourse(self, course):

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
