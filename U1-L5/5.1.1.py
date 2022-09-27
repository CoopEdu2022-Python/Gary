num_list = [1, 2, 3, 4, 5]
num_list.insert(0, 0)
print('step 0 :', num_list)

num_list.append(6)
print('step 1 :', num_list)

num_list1=[7,8,9]
print('step 2 :', num_list1)
num_list.extend(num_list1)
print('step 3 :', num_list)

num_list.pop()
print('step 4 :', num_list)
num_list.pop(0)
print('step 5 :', num_list)
num_list.remove(3)
print('step 6 :', num_list)
num_list.clear()
print('step 7 :', num_list)
num_list = [1, 2, 3, 4, 5]
num_list[0] = 0
print('step 8 :', num_list)
num_list.sort()
print('step 9 :', num_list)
num_list.sort(reverse=True)
print('step 10 :', num_list)
print('step11:', num_list.count(1))
print('step12:', len(num_list))
num_list.reverse()
print('step13:', num_list)

