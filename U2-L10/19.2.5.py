def uniquenumber(nums):
    a= 0
    for i in set(nums):
        a+=i
    return a
