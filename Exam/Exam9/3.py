def largest_altitude(gain: list[int]) -> int:
    a=0
    b=[]
    for i in gain:
        a+=i
        b.append(a)

    return  max(b)