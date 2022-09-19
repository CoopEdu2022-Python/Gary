n = int(input("Enter a number: "))
if n == 1:
    print('不是')
for i in range(2, n):
    if n % i == 0:
            print('不是')
            break
    print('是')


