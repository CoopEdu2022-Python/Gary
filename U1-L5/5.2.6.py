blackboard = [ 576, 345, 354, 3456,56789]
n = sorted(blackboard)
o = 0
d=0
f=0
while len(blackboard) != 1:
    if len(n)>2:
        o = n[0] * n[1]+1
        n.pop(0)
        n.pop(1)
        n.append(o)
        n = sorted(n)
    else:
        print(n)





print(n)
