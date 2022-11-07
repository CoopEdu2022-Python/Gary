'''def reverse_vowels(s):
    a = []
    v = 'aAeEiIoOuU'
    for i in s:
        if i in v:
            a.append(i)
    b = a[::-1]
    for q in range(len(a)):
        s = s.replace(b[q],a[q], 1)
    return s


print(reverse_vowels('CoopEdu2022'))'''


def reverse_vowels(s):
    vowels = []
    for char in s:
        if char in 'aeiouAEIOU':
            vowels.append(char)
    result = ''
    for char in range(len(s)):
        if s[char] in 'aeiouAEIOU':
            result += vowels.pop()
        else:
            result += s[char]
    return result
