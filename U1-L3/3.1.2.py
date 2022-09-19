while True:
    age = int(input('请输入你的年龄'))
    if age < 3:
        print('免费')
    elif age < 12:
        print('10')
    else:
        print('15')