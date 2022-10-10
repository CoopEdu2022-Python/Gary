# 1. 定义一个字符串变量并打印，内容为一句名言：Talk is cheap. Show me the code.
a = 'Talk is cheap. Show me the code.'
print(a)

# 2. 仍然使用一个字符串变量打印 "Talk is cheap. Show me the code."
# 但是，要将引号也打印出来
a = '\"Talk is cheap. Show me the code.\"'
print(a)

# 3. 在代码的下方添加注释，标注这个字符串的长度
poem_ = '''
1234567890 
10
'''

# 4. 因为某种原因，你需要定义一个字符串变量，来保存毕加索的全名：巴勃罗·迭戈·何塞·弗朗西斯科·狄·保拉·胡安·纳波穆西诺·玛莉亚·狄·洛斯·雷梅迪奥斯·西普里亚诺·狄·拉·圣地西玛·特里尼达·路易斯·毕加索
# 但是，在 IDE 中，在一行中显示全名有些长，想办法分多行定义这个字符串变量
a = '巴勃罗·迭戈·何塞·弗朗西斯科·狄·保拉·胡安·纳波穆西诺\
·玛莉亚·狄·洛斯·雷梅迪奥斯·西普里亚诺·狄·拉·圣地\
西玛·特里尼达·路易斯·毕加索'
print(a)
# 5. 通过字符串切片的方式，打印 '毕加索' 三个字
name = '巴勃罗·迭戈·何塞·弗朗西斯科·狄·保拉·胡安·纳波穆西诺·玛莉亚·狄·洛斯·雷梅迪奥斯·西普里亚诺·狄·拉·圣地西玛·特里尼达·路易斯·毕加索'
print(name[69:81])

# 6. 关于字符串切片，举一些其他的例子，体现切片的用法（调整不同的参数）
a= 'Talk is cheap. Show me the code.'
print(a[-1:1])
print(a[::2])
print(a[-3:-1])

# 7. 用多行注释的方式，按照字母顺序，列出目前所有的字符串方法
''''__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
  'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
  'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
   'rpartition','rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 
   'upper', 'zfill'

'''

# 8. 用多行注释的方式，简述字符串和列表的区别
'''
列表可以添加但是字符串不行
都可以用切片等方法
'''



