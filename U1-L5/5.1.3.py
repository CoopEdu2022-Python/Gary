list_num = [1, 3, 4, 3, 7, 3, 9, 8, 6, 3]

count = 0
for i in range(0, len(list_num)):
    if list_num[i-count] == 3:
        list_num.pop(i-count)
        count += 1

print(list_num)