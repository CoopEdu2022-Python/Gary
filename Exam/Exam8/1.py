def check_if_pangram(sentence: str) -> bool:
    A = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
         'v', 'b', 'n', 'm']
    o=[]
    for g in sentence:
        o.append(g)
    set(o)
    for i in sentence:
        if i in A:
            A.remove(i)
    if len(A) ==0:
        return True
    else:
        return False
print(check_if_pangram("CoopEdu"))