import systempackage


def student(name):
    newstudent = systempackage.student.Student(name)
    print("请选择您要进行的操作：\n1.选课\n2.退课\n3.查看课程\n4.退出")
    choice = input("请输入您的选择：")
    if choice == '1':
        print("选课")
        course = input("请输入您要选的课程：")
        newstudent.add_course(course)
    if choice == '2':
        course = input("请输入您要退的课程：")
        newstudent.drop_course(course)
    if choice == '3':
        course = input("请输入您要查看的课程：")
        newstudent.seestucourse(course)

    if choice == '4':
        systempackage.loginsystem.insystem().logout()
    else:
        print('输入错误，请重新输入')


def officer(name):
    control_officer = systempackage.officer.officer(name)

    choice = input("请输入您的选择：")
    if choice == '1':
        _name = input('请输入要创建的学生姓名')
        credit = input('请输入要创建的学生学分')
        lesson = input('请输入要创建的学生预分配课程')
        password = input('请输入要创建的学生密码')
        new_stu_info = control_officer.createstudent(_name, credit, lesson, password)
        systempackage.student.Student.create_student(new_stu_info[0], new_stu_info[1], new_stu_info[2], new_stu_info[3])
        print('创建成功')
    elif choice == '2':
        _name = input('请输入要设置学分要求的学生姓名')
        credit = input('请输入要设置的学分要求')
        back, back1 = control_officer.setcredit(_name, credit)
        systempackage.student.Student.set_credit(back, back1)
        systempackage.student.Student.update(_name)
    elif choice == '3':
        _name = input('请输入要查看学生的姓名')
        control_officer.seeprofile(_name)
    elif choice == '4':
        _course = input('请输入要修改的课程名称')
        control_officer.changecourse(_course)
    elif choice == '5':
        _course = input('请输入要查看的课程名称')
        control_officer.seecourse(_course)
    elif choice == '6':
        _name = input('请输入要查看的学生姓名')
        control_officer.seestucourse(_name)
    elif choice == '7':
        _name = input('请输入要创建officer的姓名')
        _password = input('请输入要创建officer的密码')
        control_officer.createofficer(_name, _password)
    elif choice == '8':
        systempackage.loginsystem.insystem().logout()
        return False
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
            control = student(name)
            if not control:
                return False

        else:
            print('登录失败')
    elif systempackage.loginsystem.insystem().login(type) == 'officer':
        if systempackage.loginsystem.insystem().verity(name, password) == 'officer':
            print('登录成功')
            control = officer(name)
            if not control:
                return False
        else:
            print('登录失败')
    else:
        print('登录失败')


while True:
    welcome()
    if not welcome():
        continue
