import os


class in_system:
    student_list = []
    officer_list = []

    for i in os.listdir():
        if i.startswith('student_'):
            student_list.append(i[8:-4])
        elif i.startswith('officer_'):
            officer_list.append(i[8:-4])

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
        if name in in_system.student_list:

            with open('student:' + name + '.txt', 'r') as studen_info:
                all = studen_info.readlines()

                right_password = all[3][9:-1]
            if right_password == password:
                return 'student'
            else:
                print('密码错误')
                return 'error'

        elif name in in_system.officer_list:
            with open('officer:' + name + '.txt', 'r') as officerinfo:
                all = officerinfo.readlines()
                right_password = all[1][9:-1]
            if right_password == password:
                return 'officer'
            else:
                print('密码错误')
                return 'error'
        else:
            print('没有此用户')
            return 'error'

    @staticmethod
    def logout():
        print('退出成功')
