courselist = []


class Course:
    def creatcourse(self, name, studentlist, teacher, coursetype, credit, studentnum):

        if name not in courselist:
            courseinfor = open('course:'+name + '.txt', 'w')
            courseinfor.write('Course name: ' + name + '\n')
            courseinfor.write('Teacher: ' + teacher + '\n')
            courseinfor.write('Course type: ' + coursetype + '\n')
            courseinfor.write('Credit: ' + str(credit) + '\n')
            courseinfor.write('Student number: ' + str(studentnum) + '\n')
            studentlist = ''.join(str(i) + ',' for i in studentlist)
            courseinfor.write('Student list: {}\n'.format(studentlist))
            courseinfor.close()
            courselist.append(name)
        else:
            print('名称已经用过')










