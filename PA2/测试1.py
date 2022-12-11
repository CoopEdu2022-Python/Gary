courseinfor = open('Python.txt', 'r+')
all = courseinfor.readlines()

studentlist = all[5][14:-1].split(',')

studentnum = all[4][16:-1]
print(studentlist, studentnum)