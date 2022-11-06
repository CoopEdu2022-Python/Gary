def reverse_vowels(s):
    a = []
    v = 'aAeEiIoOuU'
    for i in s:
        if i in v:
            a.append(i)
    b = a[::-1]
    for q in range(len(a)):
        s = s.replace(b[q],a[q], 1)
    return s


print(reverse_vowels('CoopEdu2022'))
