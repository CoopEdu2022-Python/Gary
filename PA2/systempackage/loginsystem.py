import os
import officer
import student


class insystem:


    def login(self,type,name):

        if type == 'student':
            student1= student.Student(name)
            return student
        elif type == 'officer':
            officer1 = officer.officer(name)
            return officer
        else:
            print('没有这个身份')
    def verify(self):

        pass

    def logout(self):
        print('退出成功')
