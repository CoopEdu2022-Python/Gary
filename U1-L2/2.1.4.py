a=5

user_guess = int(input('请输入一个数字：'))
if user_guess == a:
    print('恭喜你，猜对了！')
elif user_guess < a:
    print('猜小了')
elif user_guess > a:
    print('猜大了')
else:
    print('😾')