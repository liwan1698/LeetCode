"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
"""


nums1, target1 = [2,7,11,15], 9
nums2, target2 = [3,2,4], 6
nums3, target3 = [3,3], 6


def two_num_sum(nums, target):
    # repo_nums = nums
    # nums.sort()
    # i, j = 0, len(nums)-1
    # while i < j:
    #     temp = nums[i] + nums[j]
    #     if temp == target:
    #         return [, j]
    #     elif temp > target:
    #         j -= 1
    #     else:
    #         i += 1

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


assert two_num_sum(nums1, target1) == [0,1]
assert two_num_sum(nums2, target2) == [1,2]
assert two_num_sum(nums3, target3) == [0,1]


"""
题解：数组的问题如果是排序过，则适合使用while从两头往中间循环；如果没有排序，可以先使用最简单的for循环做题，然后再排序做题。
"""
