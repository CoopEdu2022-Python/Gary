def a(columnNumber, colcolumnNumber=None):
    b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if columnNumber <= 26:
        return b[columnNumber - 1]
    else:
        r = []
        e = ''
        for i in range(1,(columnNumber // 26)+1):
            r.append(b[i])
            columnNumber-=columnNumber // 26**i
        print(r)



        return ''.join(r)


print(a(29))