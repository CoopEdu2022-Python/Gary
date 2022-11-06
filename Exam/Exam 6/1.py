def is_power_of_3_v1(n):
    if n == 1:
        return True
    if n % 3 == 0:
        return is_power_of_3_v1(n / 3)
    else:
        return False


def is_power_of_3_v2(n):
    if not -2 ^ 31 <= n <= 2 ^ 31 - 1:
        return False
    while n % 3 == 0:
        n = n / 3
    if n == 1:
        return True
    else:
        return False


print(is_power_of_3_v2(9))
