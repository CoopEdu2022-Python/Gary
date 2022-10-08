dic = {
    'python': 95,
    'java': 99,
    'c': 100
}
print(len(dic))
dic['java'] = 68
print(dic)
del dic['c']
print(dic)
dic['php'] = 90
value = dic.values()
key = dic.keys()
print(value)
print(key)
print('javascript' in dic)
a = 0
for i in dic.values():
    a += int(i)
print(a)
p=[]
for i in dic.values():
    p.append(int(i))
p.sort()
print(p[-1])
print(p[0])
dic1 = {'php': 97}
dic.update(dic1)
print(dic)