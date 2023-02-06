def h(a, c, b):
    sentence = b
    for i in range(c):

        sentence=sentence[-1:]+sentence[:-1:]
    print(sentence)


h(1,0,1)