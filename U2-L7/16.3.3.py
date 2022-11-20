def shuffle_array(nums: list[int]):
    a = set(nums)
    for i in a:
        if nums.count(i) > 1:
            return i


print(shuffle_array([2,1,2,5,3,2]))
