num = 5
for i in range(5):
    num1 = int(input('请输入一个数字'))
    if num1 == num:
        print('猜对了')
        break
    elif num1 > num:
        print('猜大了')
    elif num1 < num:
        print('猜小了')
    else:
        print('输入错误')