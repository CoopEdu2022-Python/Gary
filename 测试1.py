print("欢迎使用成绩查询工具")
count = 0
while True:
    scrores = int(input("请输入成绩"))
    if scrores == 10086:
        print("你共查询了%s"%(count) )


    elif scrores >= 97:
        print("A+ GPA=4.0")

    elif scrores >= 93:
        print("A GPA=4.0")

    elif scrores >= 90:
        print("A- GPA=3.7")
    elif scrores >= 85:
        print("B+ GPA=3.3")
    elif scrores >= 80:
        print("B GPA=3.0")
    elif scrores >= 77:
        print("B- GPA=2.7")
    elif scrores >= 73:
        print("C+ GPA=2.3")
    elif scrores >= 70:
        print("C GPA=2.0")
    elif scrores >= 67:
        print("C- GPA=1.7")
    else:
        print("F GPA=0")
    count += 1
