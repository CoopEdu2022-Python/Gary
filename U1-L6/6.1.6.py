text='abcabcABCGH'
c=[]
l=''
def j(text):
    c = []
    H='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    h='abcdefghijklmnopqrstuvwxyz'
    for a in text:
        if a in H:
            c.append(H[-(H.find(a)+1)])
        elif a in h:
            c.append(h[-(h.find(a)+1)])
    return l.join(c)
print(j(text))

