username = input('username?')
user_key = input('key?')


def reset_key(username, user_key, login_info={'user1': ['pw1']}):
    while True:

        if len(user_key) >= 8:
            print('密码不少于八位')
        words = 'qwertyuiiiiiopasdfghjklzxcvbnm'
        number = '1234567890'
        y = 0
        n = 0
        for i in user_key:
            if i.lower in words:
                y += 1
            if i in number:
                n += 1
        if user_key == 'Q':
            break
        if y < 1:
            print('没有字母')
            continue
        if n < 1:
            print('没有数字')
            continue
        if user_key in login_info[username]:
            print('请设置未使用的密码')
        else:
            print('已重置密码')
            login_info[username].append(user_key)
            print(tuple(username, user_key))
        if len(login_info[username]) == 4:
            login_info[username].pop(0)
        return False

