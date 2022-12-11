courseinfor = open('Python.txt', 'r+')
courseinfor.seek(5,0)
print(courseinfor.readline())