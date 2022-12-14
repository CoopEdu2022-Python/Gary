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
    print("请选择您要进行的操作：\n1.创建学生\n2.设置学分要求\n3.查看所有老师\n4.退出")
    choice = input("请输入您的选择：")
    if choice == '1':
        _name = input('请输入要创建的学生姓名')
        credit = input('请输入要创建的学生学分')
        lesson = input('请输入要创建的学生预分配课程')
        password = input('请输入要创建的学生密码')
        new_stu_info = newofficer.createstudent(_name, credit, lesson, password)
        systempackage.student.Student.createstudent(new_stu_info[0], new_stu_info[1], new_stu_info[2], new_stu_info[3])
        print('创建成功')
    elif choice == '2':
        _name = input('请输入要设置学分要求的学生姓名')
        credit = input('请输入要设置的学分要求')
        newofficer.setcredit(_name, credit)
    elif choice == '3':
        _name = input('请输入要查看学生的姓名')
        newofficer.seeprofile(_name)
    elif choice == '4':
        _course = input('请输入要修改的课程名称')
        newofficer.changecourse(_course)
    elif choice == '5':
        _course = input('请输入要查看的课程名称')
        newofficer.seecourse(_course)
    elif choice == '6':
        _name = input('请输入要查看的学生姓名')
        newofficer.seestucourse(_name)
    elif choice == '7':
        _name = input('请输入要创建officer的姓名')
        _password = input('请输入要创建officer的密码')
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
