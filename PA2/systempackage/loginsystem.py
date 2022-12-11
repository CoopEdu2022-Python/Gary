import os
import officer
import student


class insystem:
    studentlist = []
    officerlist = []
    for i in os.listdir():
        if i.startswith('student:'):
            studentlist.append(i[9:])
        elif i.startswith('officer:'):
            officerlist.append(i[9:])
    @staticmethod
    def login(type):

        if type == 'student':
            return 'student'

        elif type == 'officer':
            return 'officer'
        else:
            print('没有这个身份')

    @staticmethod
    def verity(name, password):
        if name in insystem.studentlist:

            with open('student:' + name + '.txt', 'r') as studeninfo:
                all = studeninfo.readlines()

                rightpassword = all[6][9:-1]
            if rightpassword == password:
                return 'student'
            else:
                print('密码错误')

        elif name in insystem.officerlist:
            with open('officer:' + name + '.txt', 'r') as officerinfo:
                all = officerinfo.readlines()
                rightpassword = all[1][9:-1]
            if rightpassword == password:
                return 'officer'
            else:
                print('密码错误')
        else:
            print('没有此用户')
    @staticmethod
    def logout():
        print('退出成功')
