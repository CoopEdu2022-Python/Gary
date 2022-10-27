class Student:
    def __init__(self, name=None, student_id='0'):
        self.name = name
        self.student_id = student_id
        self.score = 70
        print('{} enrolled! (id: {})'.format(name, student_id))

    def __del__(self):
        print('{} dropped out! (id: {})'.format(self.name, self.student_id))

    def __str__(self):
        info = 'name: {}\nid: {} '.format(self.name, self.student_id)
        return info

    def study(self):
        self.score += 1
        self.mood = 'good'

    def play(self, days=1):
        if self.score < 70 or self.score > 90:
            self.mood = 'perfect'
        else:
            self.mood = 'bad'
        self.score -= (days - 1)

    def self_introduction(self):
        print(self)

# main program writes below
# ...
# ...
'''
None enrolled! (id: 0)
None 0
'''
student_1 = Student()
print(student_1.name, student_1.student_id)

'''
7 enrolled! (id: 0)
None dropped out! (id: 0)
name: 7
id: 0 
'''
student_1 = Student('7')
print(student_1)

'''
None enrolled! (id: 0)
7 dropped out! (id: 0)
name: None
id: 0 
'''
student_1 = Student()
student_1.self_introduction()

'''
xxs enrolled! (id: 9)
None dropped out! (id: 0)
'''
student_1 = Student('xxs', '9')

'''
100 good
'''
for day in range(30):
    student_1.study()

print(student_1.score, student_1.mood)

'''
100 perfect
'''
for day in range(31, 0, -1):
    student_1.play()

print(student_1.score, student_1.mood)

if student_1.score < 70:
    del student_1

'''
报错
'''
student_1 = Student()
info = str(student_1)
print(student_1.info)

'''
None enrolled! (id: 0)
None dropped out! (id: 0)
None enrolled! (id: 0)

'''
student_1 = Student()
student_2 = Student()

'''
1
'''
student_1.study()
len_1 = len(dir(student_1))  # dir 返回对象的所有属性 + 方法的列表
len_2 = len(dir(student_2))
print(len_1 - len_2)
