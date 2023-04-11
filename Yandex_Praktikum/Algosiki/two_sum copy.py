def twoSum(nums, target):
    nums1 = sorted(nums)

    left = 0
    right = len(nums) - 1
    while left < right:
        print(left, right)
        print(nums1)
        current_sum = nums1[left] + nums1[right]
        # print(current_sum, nums[left], nums[right], target)
        if current_sum == target:
            if nums1[left] == nums1[right]:
                return 
            return nums.index(nums1[left]), nums.index(nums1[right])
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return None, None

print(twoSum(list(map(int, input().split())),int(input())))