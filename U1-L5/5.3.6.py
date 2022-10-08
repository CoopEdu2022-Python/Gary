def compare_dict(dict1, dict2):
    a = []
    for key,value in dict1.items():
        if key in dict2:
            if not value == dict2[key]:


                a.append(key)
                a.append(value)
        else:
            a.append(key)
            a.append(value)
    b = len(a)
    a.append('有' + str(b) + '个不同')
    return tuple(a)



print(compare_dict())
