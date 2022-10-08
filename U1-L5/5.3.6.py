def compare_dict(dict1, dict2):
    a = []
    for key in dict1:
        if key not in dict2 or dict1[key] != dict2[key]:
            a.append(key)
    b = len(a)
    a.append('有' + str(b) + '个不同')
    return a



print(compare_dict({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'c': 3, 'd': 4}))
