def array_sign(nums: list[int]) -> int:
    a = 1
    for i in nums:
        a = a*i
    if a>0:
        return 1
    elif a==0:
        return 0
    else:
        return  -1

print(array_sign([1,5,0,2,-3]))