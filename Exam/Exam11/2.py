

def find_shortest_subarray(nums: list[int]) -> int:
    maxnum = []
    for k in nums:
        a=nums.count(k)
        maxnum.append(a)
    a=max(maxnum)
    h=maxnum.index(a)
    h1 = maxnum[::-1].index(a)
    max1=nums[h]
    nums1=nums
    nums1.remove(nums[h:h1])




with open('2.txt', 'r') as f:
    for i in f.readlines():
        pass