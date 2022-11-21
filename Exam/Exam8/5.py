def largest_perimeter(nums: list) -> int:
    nums.sort()
    a=nums[0]+nums[1]
    if a<nums[2]:
        return 0
    else:
        return nums[0]+nums[1]+nums[2]
print(largest_perimeter([1,2,1]))