age = int(input('今年多大了？'))
if age >= 18:
    print('可以进网吧嗨皮')
else:
    print('你还没长大应该回家写作业')
print('这句代码什么时候执行？')

age = 100
if age >=0 and age <= 120:
    print('年龄正确')
else:
    print('年龄不正确')

python_score = 50
c_score = 50
if python_score > 60 or c_score > 60:
    print('考试通过')
else:
    print('再接再厉')

is_employee = True
if not is_employee:
    print('非公勿内')
