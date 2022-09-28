tuple_sample = (1, 1, 2, 3, 6, 5, 4, 1)
o = list(tuple_sample)
for i in o:
    for y in o:
        if i == y and o.count(i) > 1:
            o.remove(i)
print(tuple(o))
