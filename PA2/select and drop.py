courselist = []


class Course:
    def __init__(self, name, studentlist, teacher, coursetype, credit, studentnum):
        self.studentlist = studentlist
        self.teacher = teacher
        self.coursetype = coursetype
        self.credit = credit
        self.name = name
        courseinfor = open(name + '.txt', 'w')
        courseinfor.write('Course name: ' + name + '\n')
        courseinfor.write('Teacher: ' + teacher + '\n')
        courseinfor.write('Course type: ' + coursetype + '\n')
        courseinfor.write('Credit: ' + str(credit) + '\n')
        courseinfor.write('Student number: ' + str(studentnum) + '\n')
        self.studentlist = ''.join(str(i) + ',' for i in studentlist)
        courseinfor.write('Student list: {}\n'.format(self.studentlist))
        courseinfor.close()
        courselist.append(name)


class Student:
    def __init__(self, name):
        self.name = name

    def addcourse(self, course):
        print('Course list: {}'.format(courselist))
        whatcourse = input('要选哪节课? ')
        if whatcourse in courselist:
            courseinfor = open(whatcourse + '.txt', 'w+')
            all = courseinfor.readlines()
            courseinfor.seek(0, 2)
            studentlist = courseinfor.readline()
            studentlist = studentlist.split(',')
            courseinfor.seek(1, 2)
            studentnum = courseinfor.readline()

            if self.name in studentlist:
                print('你已经选过这门课了')
            elif len(studentlist) >= int(studentnum):
                print('这门课已经满了')
            else:
                studentlist.append(self.name)
                courseinfor.write('Student list: {}'.format(''.join(str(i) + ',' for i in studentlist)))
                print('选课成功')
        else:
            print('没有这节课')

    def dropcourse(self, course):
        print('Course list: {}'.format(courselist))
        whatcourse = input('要退哪节课? ')
        if whatcourse in courselist:
            courseinfor = open(whatcourse + '.txt', 'w+')
            studentlist = courseinfor.read()
            studentlist = studentlist.split(',')

            if self.name in studentlist:
                studentlist.remove(self.name)
                courseinfor.write('Student list: {}'.format(''.join(str(i) + ',' for i in studentlist)))
                print('退课成功')
            else:
                print('你没有选这门课')
        else:
            print('没有这节课')

    def seestucourse(self):
        print('Course list: {}'.format(courselist))
        whatcourse = input('要看哪节课? ')
        if whatcourse in courselist:
            courseinfor = open(whatcourse + '.txt', 'r')
            print(courseinfor.read())
            courseinfor.close()


Course1 = Course('math', ['Zhang'], 'Li', 'True', 1, 1)

Student1 = Student('Zhang')
Student1.seestucourse()
