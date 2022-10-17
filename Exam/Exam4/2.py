def reset(login_info):
    while user_name:=input('?'):
        if user_name == 'q':
            return False
        if user_name not in login_info.keys():
            print('?')
        else:
            break
    while password:=input('?'):
        if user_name == 'q':
            return False
        if len(password)<=8:
            print('必须大于八个')
        if not password.isalnum():
            print('只有字母和数字')
        if passwprd in login_info[user_name]:
            print('不能与上次密码相同')
        else:
            break
    if len(login_info[user_name])>=3:
        login_info[user_name].pop()
        login_info[user_name].insert(0,password)
        print('密码修改')
        return user_name,password,login_info[user_name]

