def largest_perimeter(nums: list) -> int:
    a= nums.sort()
    if nums[0]+nums[1]<nums[2]:
        return 0
    else:
        return nums[0]+nums[1]+nums[2]
print(largest_perimeter([1,2,1]))