while True:
    a = float(input('输入第一个数字'))
    b = float(input('输入第二个数字'))
    c= input('加，减，乘，除')
    d=0.0
    if c == '加':
        d=a+b
        print(d)
    elif c=='减':
        d=a-b
        print(d)
    elif c=='乘':
        d=a*b
        print(d)
    elif c=='除':
        if b==0.0:
            print('除数不能为零')
        else:
            c=a/b
            print(c)
            continue
    else:
        print('错了')
        continue