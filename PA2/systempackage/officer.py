import os
class officer:
    def __init__(self, name):
        self.name = name

    def createstudent(self, name,credit):
        return name,credit

    def setcredit(self, name, credit):
        return name,credit
    def seeprofile(self, name):
        info= open('student:'+name+'.txt', 'r')
        all = info.read()
        print(all)
        info.close()
    def creatcourse(self, name, studentlist, teacher, coursetype, credit, studentnum):
        return name, studentlist, teacher, coursetype, credit, studentnum
    def changecourse(self,name):
        os.startfile('course:'+name+'.txt')
    def seecourse(self,name):
        os.startfile('course:'+name+'.txt','print')
    def seestucourse(self,name):
        os.startfile('student:'+name+'.txt','print')
    def createofficer(self,name,password):
        studentinfo = open('officer:' + name + '.txt', 'w')
        studentinfo.write('Name:' + name + '\n')

        studentinfo.write('password:' + str(password))
