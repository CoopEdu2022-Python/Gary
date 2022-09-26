a = 0
b = 0
p = 0
for i in range(30):
    a = int(input('学生分数'))
    if a > 100:
        print('分数有误，请重新输入')
        continue
    if a < 0:
        print('分数有误，请重新输入')
        continue
    b += a
p = b / 30
print('平均分为%.2f' % (p))