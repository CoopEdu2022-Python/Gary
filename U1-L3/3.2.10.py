
n=int(input('?'))
s=0
for i in range(2,n):
    s=n%i
    if s==0:
        print(i,end='')
        n=n/i
        if n!=1:
            print('*',end='')
        continue


