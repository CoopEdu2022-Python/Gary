def compare_dict(dict1, dict2):
    a = []
    for key, value in dict1.items():
        if key in dict2:
            if  value == dict2[key]:
                a.append(key)
                a.append(value)


    b = len(a)
    a.clear()
    a.append('有' + str(b//2) + '个相同')
    return tuple(a)


print(compare_dict({'1': 2, '2': 3}, {'1': 2, '2': 3}))
