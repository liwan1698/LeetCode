"""
给定两个数组，编写一个函数来计算它们的交集。
"""

nums1 = [1,2,2,1]
nums2 = [2,2]
output1 = [2,2]

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
output2 = [4,9]


def find_cross(nums1, nums2):
    nums1.sort()
    nums2.sort()
    ret = []
    m, n = len(nums1), len(nums2)
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            ret.append(nums1[i])
            i += 1
            j += 1
    return ret


assert find_cross(nums1, nums2) == output1
assert find_cross(nums3, nums4) == output2


"""
题解：一开始使用了for循环和in来做，但是发现结果中有重复的元素。因此使用上了sort大法，然后采用双指针来做。
"""
