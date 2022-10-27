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

#函数是什么？方法是什么？函数和方法的共同点、不同点？[多行注释]
'''
函数封装了一些代码可以形式独立功能的代码
方法封装了一些代码可以形式独立功能的代码，但是他只能依靠类调用

'''
#内置函数是什么？内置方法是什么？列举所有内置函数和所有内置方法 [多行注释]
'''
python提供可以直接调用的函数
python提供可以直接使用的方法，依靠类调用

内置方法['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
内置函数abs()

delattr()

hash()

memoryview()

set()

all()

dict()

help()

min()

setattr()

any()

dir()

hex()

next()

slice()

ascii()

divmod()

id()

object()

sorted()

bin()

enumerate()

input()

oct()

staticmethod()

bool()

eval()

int()

open()

str()

breakpoint()

exec()

isinstance()

ord()

sum()

bytearray()

filter()

issubclass()

pow()

super()

bytes()

float()

iter()

print()

tuple()

callable()

format()

len()

property()

type()

chr()

frozenset()

list()

range()

vars()

classmethod()

getattr()

locals()

repr()

zip()

compile()

globals()

map()

reversed()

__import__()

complex()

hasattr()

max()

round()


'''
#Python 的 self 参数是什么？[多行注释]
'''
Self是对象的调用
'''