def update_dict(dict_sample):
    key = input('key?')
    value = int(input('value?'))
    if key in dict_sample:
        for key1,value1 in dict_sample.items():
            if value1 >= value:
                dict_sample[key1] = value1
            else:
                dict_sample[key1] = value
    else:
        dict_sample[key] = value
    return dict_sample


print(update_dict({
    'python': 95,
    'java': 99,
    'c': 100
}))
