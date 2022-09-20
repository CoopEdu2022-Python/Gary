
n = int(input("Enter a number: "))
if n <= 1:
    print('不是')
for i in range(2, n+1):
    if n % i == 0:
            print('不是')
            break
    else:
        print('是')


