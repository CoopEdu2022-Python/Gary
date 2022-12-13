

def find_shortest_subarray(nums: list[int]) -> int:
    maxnum = []
    for k in nums:
        a=nums.count(k)
        maxnum.append(a)
    a=max(maxnum)
    h=maxnum.index(a)
    max1=nums[h]
    while nums.count(max1)>0:
        nums.remove(max1)
    for k in range(len(nums)):
        pass



with open('2.txt', 'r') as f:
    for i in f.readlines():
        pass