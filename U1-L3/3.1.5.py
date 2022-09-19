num=6
while True:
    num1= int(input('请输入一个数字'))
    if num1 == num:
        print('猜对了')
        break
    elif num1 > num:
        num2=num1-num
        print('猜大了%d'%num2)
    elif num1 < num:
        num2=num-num1
        print('猜小了%d'%num2)