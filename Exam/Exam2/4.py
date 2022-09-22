a = int(input('三位数'))
b = 0
q = 0
w = 0
e = 0
r = 0
c = (a // 100)
b = (a // 10) % 10
d = a % 10
q = c ** 3
w = b ** 3
e = d ** 3
r = q + w + e
if r == a:
    print('是的')
else:
    print('不是')
