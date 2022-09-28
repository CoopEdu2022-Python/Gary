users = ('root', 'user1', 'user2')
passwords = ('123', 'abc', '@*#')
user=input('用户名')
password=input('密码')
for i in range(4):
    if user == users[0]:
        if password == passwords[0]:
            print('进入系统')
            break
        else:
            print('密码错误')
    elif user == users[1]:
        if password == passwords[1]:
            print('进入系统')
            break
        else:
            print('密码错误')
    elif user == users[2]:
        if password == passwords[2]:
            print('进入系统')
            break
        else:
            print('密码错误')
    else:
        print('用户名输入错误')