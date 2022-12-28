import systempackage


def student(name):
    new_student = systempackage.student.Student(name)
    new_control = systempackage.controller.Controller(name)
    print("请选择您要进行的操作：\n1.选课\n2.退课\n3.查看课程\n4.退出")
    choice = input("请输入您的选择：")
    if choice == '1':
        print("选课")
        course = input("请输入您要选的课程：")

        new_control.add_course(new_student.add_course(course))
        return True
    if choice == '2':
        course = input("请输入您要退的课程：")
        new_control.drop_course(new_student.drop_course(course))
        return True
    if choice == '3':
        course = input("请输入您要查看的课程：")
        new_control.see_stu_course(new_student.see_stu_course(course))
        return True
    if choice == '4':
        new_control.logout()
        del new_control
        del new_student
        return False
    else:
        print('输入错误，请重新输入')


def officer(name):
    new_officer = systempackage.officer.officer(name)
    new_control = systempackage.controller.Controller(name)
    print(
        "请选择您要进行的操作：\n1.创建学生\n2.设置学分\n3.查看学生\n4.修改课程\n5.查看课程\n6.查看学生选课情况\n7.创建officer\n8.退出")
    choice = input("请输入您的选择：")
    if choice == '1':
        _name = input('请输入要创建的学生姓名')
        credit = input('请输入要创建的学生学分')
        lesson = input('请输入要创建的学生预分配课程')
        password = input('请输入要创建的学生密码')
        officer_name, officer_credit, officer_lesson, officer_password = new_officer.create_student(_name, credit,
                                                                                                    lesson, password)
        new_control.create_student(officer_password, officer_name, officer_credit, officer_lesson)
        print('创建成功')
        return True
    elif choice == '2':
        _name = input('请输入要设置学分要求的学生姓名')
        credit = input('请输入要设置的学分要求')
        officer_name, officer_credit = new_officer.set_credit(_name, credit)
        new_control.set_credit(officer_name, officer_credit)
        return True
    elif choice == '3':
        _name = input('请输入要查看学生的姓名')
        officer_name = new_officer.see_profile(_name)
        new_control.see_profile(officer_name)
        return True
    elif choice == '4':
        _course = input('请输入要修改的课程名称')
        officer_course=new_officer.change_course(_course)
        new_control.change_course(officer_course)
        return True
    elif choice == '5':
        _course = input('请输入要查看的课程名称')
        officer_course=new_officer.see_course(_course)
        new_control.see_course(officer_course)
        return True
    elif choice == '6':
        _name = input('请输入要查看的学生姓名')
        officer_name=new_officer.see_stu_course(_name)
        new_control.see_stu_course(officer_name)
        return True
    elif choice == '7':
        _name = input('请输入要创建officer的姓名')
        _password = input('请输入要创建officer的密码')
        new_officer.create_officer(_name, _password)
        return True
    elif choice == '8':
        systempackage.loginsystem.in_system().logout()
        return False
    else:
        print('输入错误，请重新输入')


def welcome():
    print("Welcome to the system\n请登录")
    type = input("请输入您的身份：(student/officer)")
    name = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    if systempackage.loginsystem.in_system().login(type) == 'student':
        if systempackage.loginsystem.in_system().verity(name, password) == 'student':
            print('登录成功')
            control = student(name)
            if not control:
                return False

        else:
            print('登录失败')
    elif systempackage.loginsystem.in_system().login(type) == 'officer':
        if systempackage.loginsystem.in_system().verity(name, password) == 'officer':
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
