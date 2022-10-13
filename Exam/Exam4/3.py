def inverse(n, str='1234567896edrgfdnh'):
    new_list = []
    new_list1 = []
    for i in range(len(str) // n ):
        if i == 0:
            new_list.append(str[0:n])
        else:
            new_list.append(str[n * i:n * i+3])

    for k in new_list:
        new_list1.append(k[::-1])
    return new_list


print(inverse(5))
