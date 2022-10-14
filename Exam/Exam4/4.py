def add(num1=123.3456, num2=234.234234):
    a = str(num1).split('.')
    b = str(num2).split('.')
    if str(num1).startswith('-'):
        a[1] = '-' + a[1]
    elif str(num2).startswith('-'):
        b[1] = '-' + b[1]
    final = int(a[0]) + int(b[0])
    if not str(num1).startswith('-') or not str(num2).startswith('-'):
        if len(a[1]) >= len(b[1]):

            o = str(b[1]) + (len(a[1]) - len(b[1])) * '0'
            t = int(a[1]) + int(b[1])
            if len(a[1])!= len(t):
                final+=t[0:len(t)-len(a[1])]
        else:
            o = str(a[1]) + (len(b[1]) - len(a[1])) * '0'
            t = int(a[1]) + int(b[1])

