i = 1
while i<= 5:
    print('hello python')
    i=i+1
print('循环结束后i=%d'%i)

result = 0
i=0
while i<=100:
    print(i)
    result+=i
    i+=1
print('0~100之间的数字求和结果=%d'%result)

result = 0
i = 0
while i<=100:
    if i%2==0:
        print(i)
        result+=1
    i+=1
print('0~100之间偶数求和的结果=%d'%result)

i=0
while i<10:
    if i==3:
        break
    print(i)
    i+=1
print('over')

i=0
while i<10:
    if i==7:
        i+=1
        continue
    print(i)
    i+=1

row = 1
while row<=5:
    print('*'*row)
    row+=1

print('*',end=' ')
print('')

row=1
while row<=5:
    col = 1
    while col <= row:
        print('*',end='')
        col+=1
    print('')
    row+=1

row=1
while row<=9:
    col=1
    while col<=row:
        print('%d*%d=%d'%(col,row,row*col))
        col+=1
    print('')
    row+=1

