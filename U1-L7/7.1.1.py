def H(s1,s2):
    for i in s1:
        if i in s2:
            return True
    return False
print(H('anagram','nagaram'))