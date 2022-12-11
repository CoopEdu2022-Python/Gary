import systempackage
def student(name):
    newstudent = systempackage.student.Student(name)
    print("请选择您要进行的操作：\n1.选课\n2.退课\n3.查看课程\n4.退出")
    choice = input("请输入您的选择：")
    if choice == '1':
        print("选课")
        course = input("请输入您要选的课程：")
        newstudent.addcourse(course)
    if choice == '2':
        course = input("请输入您要退的课程：")
        newstudent.dropcourse(course)
    if choice == '3':
        course = input("请输入您要查看的课程：")
        newstudent.seestucourse(course)

    if choice == '4':
        systempackage.loginsystem.insystem().logout()
    else:
        print('输入错误，请重新输入')
def officer(name):
    newofficer = systempackage.officer.officer(name)
    print("请选择您要进行的操作：\n1.查看所有课程\n2.查看所有学生\n3.查看所有老师\n4.退出")
    choice = input("请输入您的选择：")
    if choice == '1':
        newofficer.createofficer()
    elif choice == '2':
        newofficer.setcredit()
    elif choice == '3':
        newofficer.seeprofile()
    elif choice == '4':
        newofficer.changecourse()
    elif choice == '5':
        newofficer.seecourse()
    elif choice == '6':
        newofficer.seestucourse()
    elif choice == '7':
        newofficer.createofficer()
    elif choice == '8':
        systempackage.loginsystem.insystem().logout()
    else:
        print('输入错误，请重新输入')
def welcome():
    print("Welcome to the system\n请登录")
    type = input("请输入您的身份：(student/officer)")
    name = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    if systempackage.loginsystem.insystem().login(type) == 'student':
        if systempackage.loginsystem.insystem().verity(name, password) == 'student':
            print('登录成功')
            student(name)
        else:
            print('登录失败')
    if systempackage.loginsystem.insystem().login(type) == 'officer':
        if systempackage.loginsystem.insystem().verity(name, password) == 'officer':
            print('登录成功')
        else:
            print('登录失败')
    else:
        print('登录失败')


