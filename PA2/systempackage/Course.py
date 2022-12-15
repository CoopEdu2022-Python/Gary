
import os

class Course:
    courselist = []
    for i in os.listdir():
        if i[0:6] == 'course:':
            courselist.append(i[5:])
    def creatcourse(self, name, studentlist, teacher, coursetype, credit, studentnum):

        if name not in self.courselist:
            courseinfor = open('course:'+name + '.txt', 'w')
            courseinfor.write('Course name: ' + name + '\n')
            courseinfor.write('Teacher: ' + teacher + '\n')
            courseinfor.write('Course type: ' + coursetype + '\n')
            courseinfor.write('Credit: ' + str(credit) + '\n')
            courseinfor.write('Student number: ' + str(studentnum) + '\n')
            studentlist = ''.join(str(i) + ',' for i in studentlist)
            courseinfor.write('Student list: {}\n'.format(studentlist))
            courseinfor.close()

        else:
            print('名称已经用过')










