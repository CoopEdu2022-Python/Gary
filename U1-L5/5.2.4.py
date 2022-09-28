shopping=tuple()
y=list(shopping)
while True:
    a=input('?')
    if a == 'q':
        break
    else:
        y.append(a)
print(tuple(y),len(y))


