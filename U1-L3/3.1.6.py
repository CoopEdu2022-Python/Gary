a=0
b=0
while True:
    a = int(input('学生分数'))
    if a>100:
        print('分数有误，请重新输入')
        continue
    if a<0:
        print('分数有误，请重新输入')
        continue
    b +=a
print('平均分为%f'%fround(b/30,2))