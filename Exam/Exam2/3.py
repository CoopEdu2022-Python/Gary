m = input('m')
n = int(input('n'))


g = 0
c = 0
r = 0

for i in range(1,n+1):
    a = m * i
    g = g + int(a)
    r = int(g)
print(r)