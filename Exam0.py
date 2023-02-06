def Shalou(number,e):
    line =1
    a=number
    while a>=2 *(line+1)**2-1:
        line+=1

    for i in range(line,0,-1):
        h=e*(2*i-1)
        print(h.center(2*line,' '))
    for i in range(1,line):
        h=e * (2 * i + 1)
        print(h.center(2*line, ' '))


Shalou(19,'x')
