def prime_num(n):

    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
                return False
                break
        return True
b= 0
c=0
d=0
e=0
a = int(input('?'))
if prime_num(a)==True:
    while True:
        if a %2==0:
            a=a/2
            b=b+1
        else:
            break
if prime_num(a)==True:
    while True:
        if a %3==0:
            a=a/3
            c=c+1
        else:
            break
if prime_num(a)==True:
    while True:
        if a %5==0:
            a=a/5
            d=d+1
        else:
            break
if prime_num(a)==True:
    while True:
        if a %7==0:
            a=a/7
            e=e+1
        else:
            break
print('2*%d,3*%d,5*%d,7*%d'%(b,c,d,e))



