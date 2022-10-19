def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def h(n):
    if n == 1 :
        return 1
    elif n == 0:
        return 0

    else:
        return h(n - 1)+h(n-2)
