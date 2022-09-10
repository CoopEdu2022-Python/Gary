#变量名，函数名只能由字母/数字/下划线组成
#不能数字开头
#不能与关键字重名
'''
fromNo12                       T
from#12                        F
my_Boolean                     T
my-Boolean                    F
Obj2                          T
2ndObj                             F
myInt                              T
My_tExt                        T
_test                                   T
test!32                               F
haha(da)tt                        F
jack_rose                T
jack&rose                    F
GUI                        T
G.U.I                        F
'''



import keyword           #关键字
print(keyword.kwlist)

#两个字之间只可以用_链接
#大小写不一样



#驼峰命名法
#小驼峰第一个字母小写其余字首字母有开头大写
#每一个字首字母大写