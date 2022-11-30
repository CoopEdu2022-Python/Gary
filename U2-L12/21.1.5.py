a = open('3.txt', 'r+')
b = a.read()
c = [i for i in b]
d=[]
words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for y,i in enumerate(c):

    if i in words and i !='z' and i !='Z':
        d.append(words[words.index(i)+1])
    else:
        if i !='z' and i !='Z':
            d.append(i)


a.close()
a = open('trans3.txt', 'w')
a.writelines(d)
a.close()