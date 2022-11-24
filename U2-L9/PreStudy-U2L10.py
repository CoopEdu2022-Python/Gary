# 1. 什么是异常？
"""
程序运行时，如果python解释器遇到一个错误，会停止程序的执行，并提示一些错误信息，这就是异常。


"""

# 2. 异常有哪些类型？（如何找到全部的异常类型？)
"""
BaseException             所有异常的基类         
 +-- SystemExit              解释器请求退出
 +-- KeyboardInterrupt          用户中断执行(通常是输入^C)
 +-- GeneratorExit            生成器(generator)发生异常来通知退出
 +-- Exception               常规错误的基类
      +-- StopIteration              迭代器没有更多值 
      +-- StopAsyncIteration              必须通过异步迭代器对象的__anext__()方法引发以停止迭代
      +-- ArithmeticError                 所有数值计算错误的基类
      |    +-- FloatingPointError             浮点计算错误
      |    +-- OverflowError                  数值运算超出最大限制
      |    +-- ZeroDivisionError              除(或取模)零 (所有数据类型
      +-- AssertionError                  断言语句失败
      +-- AttributeError                  对象没有这个属性
      +-- BufferError                    与缓冲区相关的操作时引发
      +-- EOFError                        没有内建输入,到达EOF 标记
      +-- ImportError                     导入失败
      |    +-- ModuleNotFoundError        找不到模块
      +-- LookupError                     无效数据查询的基类
      |    +-- IndexError                      序列中没有此索引(index)
      |    +-- KeyError                        映射中没有这个键
      +-- MemoryError                     内存溢出错误
      +-- NameError                       未声明、初始化对象
      |    +-- UnboundLocalError              访问未初始化的本地变量
      +-- OSError                         操作系统错误，
      |    +-- BlockingIOError               操作将阻塞对象设置为非阻塞操作
      |    +-- ChildProcessError             子进程上的操作失败
      |    +-- ConnectionError               与连接相关的异常的基类
      |    |    +-- BrokenPipeError             在已关闭写入的套接字上写入
      |    |    +-- ConnectionAbortedError      连接尝试被对等方中止
      |    |    +-- ConnectionRefusedError      连接尝试被对等方拒绝
      |    |    +-- ConnectionResetError        连接由对等方重置
      |    +-- FileExistsError               创建已存在的文件或目录
      |    +-- FileNotFoundError             请求不存在的文件或目录
      |    +-- InterruptedError              系统调用被输入信号中断
      |    +-- IsADirectoryError             在目录上请求文件操作
      |    +-- NotADirectoryError            在不是目录的事物上请求目录操作
      |    +-- PermissionError              在没有访问权限的情况下运行操作
      |    +-- ProcessLookupError            进程不存在
      |    +-- TimeoutError                  系统函数在系统级别超时
      +-- ReferenceError                弱引用试图访问已经垃圾回收了的对象
      +-- RuntimeError                  一般的运行时错误
      |    +-- NotImplementedError      尚未实现的方法
      |    +-- RecursionError           解释器检测到超出最大递归深度
      +-- SyntaxError                   Python 语法错误
      |    +-- IndentationError         缩进错误
      |         +-- TabError          Tab 和空格混用
      +-- SystemError              一般的解释器系统错误
      +-- TypeError               对类型无效的操作
      +-- ValueError              传入无效的参数
      |    +-- UnicodeError             Unicode 相关的错误
      |         +-- UnicodeDecodeError     Unicode 解码时的错误
      |         +-- UnicodeEncodeError     Unicode 编码时错误
      |         +-- UnicodeTranslateError  Unicode 转换时错误
      +-- Warning                       警告的基类
           +-- DeprecationWarning          关于被弃用的特征的警告
           +-- PendingDeprecationWarning   关于构造将来语义会有改变的警告
           +-- RuntimeWarning           可疑的运行行为的警告
           +-- SyntaxWarning            可疑的语法的警告
           +-- UserWarning              用户代码生成的警告
           +-- FutureWarning            有关已弃用功能的警告的基类
           +-- ImportWarning            模块导入时可能出错的警告的基类
           +-- UnicodeWarning           与Unicode相关的警告的基类
           +-- BytesWarning             bytes和bytearray相关的警告的基类
           +-- ResourceWarning           与资源使用相关的警告的基类。。

可以用dir()
"""

# 3. 如何捕获异常？
"""
try:
    尝试执行的代码
except 异常类型1:
    针对异常类型1，对应的处理代码
except 异常类型2:
    针对异常类型2，对应的处理代码
except:
    出现异常，执行的代码
except Exception as result:捕获未知异常
    pass
else:  
    没有异常，执行的代码
finally:
    无论是否有异常，都会执行的代码

"""

# 4. 如何抛出异常？
"""
变量名 = Exception("想抛出的信息")
想抛出的变量信息就会在异常中显示
"""

# 5. 什么是异常的传递？
"""
异常的传递--当函数/方法执行出现异常，会将异常传递给函数/方法的调用一方，如果传递到主程序，仍然没有异常的处理，程序才会被终止
"""
