"""
标记：第一次没有做出来
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
"""

nums1, m1, nums2, n1 = [1,2,3,0,0,0], 3, [2,5,6], 3
nums3, m3, nums4, n3 = [1], 1, [], 0


def combine_arr(nums1, m, nums2, n):
    p1, p2 = m - 1, n - 1
    tail = m + n - 1
    while p1 >= 0 or p2 >= 0:
        print('%d-%d' % (p1, p2))
        print('%d' % tail)
        print(nums1)
        if p1 == -1:
            nums1[tail] = nums2[p2]
            p2 -= 1
        elif p2 == -1:
            nums1[tail] = nums1[p1]
            p1 -= 1
        elif nums1[p1] > nums2[p2]:
            nums1[tail] = nums1[p1]
            p1 -= 1
        else:
            nums1[tail] = nums2[p2]
            p2 -= 1
        tail -= 1
    return nums1

assert combine_arr(nums1, m1, nums2, n1) == [1,2,2,3,5,6]
assert combine_arr(nums3, m3, nums4, n3) == [1]
