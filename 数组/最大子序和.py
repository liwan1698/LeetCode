"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""


nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [1]
nums3 = [0]
nums4 = [-1]
nums5 = [-100000]


def max_sublist(nums):
    if len(nums) == 1:
        return nums[0]
    max_sum = nums[0]
    max_sub_sum = nums[0]
    for i in range(1, len(nums)):
        max_sub_sum = max(nums[i], max_sub_sum+nums[i])
        max_sum = max(max_sum, max_sub_sum)
    return max_sum


assert max_sublist(nums1) == 6
assert max_sublist(nums2) == 1
assert max_sublist(nums3) == 0
assert max_sublist(nums4) == -1
assert max_sublist(nums5) == -100000


"""
题解：此题目需要保留序列的顺序，因此不能先使用排序。
因为数组里有负数，如果是负数加上正数，则还不如直接从正数开始，所以会舍弃之前的子序列。而新的序列有可能会小于之前的子序列。所以就需要有两个值存储新序列的最大值和历史序列的最大值。
所以先比较新加上的数字和最新子序列的最大值，然后再和历史最大值进行比较。
"""
