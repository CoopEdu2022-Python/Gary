def min_cost_climbing_stairs(cost: list[int]) -> int:
    a = 0
    o=0
    b=0
    while True:
        if o==0:
            if cost[0]>cost[1]:
                b+=1
            else:
                pass
        a =a+cost[b]
        if len(cost)-b==0:
            a+=cost[b]
            break
        if len(cost)-b-3>0:
            v=min(cost[b+1:b+3])
            c=cost.index(v,b+1,b+3)
        else:
            v = min(cost[b + 1:])
            c = cost.index(v, b + 1,len(cost)+1)
            print(c)
        b=c
        if b>=len(cost):
            break
        o+=1
    return a
print(min_cost_climbing_stairs([2,0,6,9,0]))