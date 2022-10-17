def inverse(n, str='1234567896edrgfdnh'):
    new_list = []
    new_list1 = []
    for i in range(len(str) // n +1):
        if i == 0:
            new_list.append(str[0:n])
        else:
            new_list.append(str[n * i:n*i+n])

    for k in new_list:
        new_list1.append(k[::-1])
    return new_list1


print(inverse(11))
