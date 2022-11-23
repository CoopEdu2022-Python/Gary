def largest_perimeter(nums: list) -> int:
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        if nums[i]-nums[i+1]<nums[i+2]:
            return nums[i]+nums[i+1]+nums[i+2]


print(largest_perimeter([2,1,2]))