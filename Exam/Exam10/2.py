
def max_profit(prices: list[int]) -> int:

    m=[]

    while len(prices)>=2:

        min1 = min(prices)
        finmin = prices.index(min1)
        Max1 = max(prices[finmin:])
        final = Max1 - min1
        m.append(final)
        prices.remove(min(prices))
    else:
        return max(m)


print(max_profit([0,4,18,46,22,69,34,96,57,48,11,47,8,10,3,77,88,87,70,75,75,70,20,81,77,74,61,15,8,45,61,4,52,21,62,40,51,89,18,89,2,44,29,6,71,69,24,36,72,68,80,33,94,65,100]))