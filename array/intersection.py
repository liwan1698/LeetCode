"""
求两个数组的交集

输入：nums1=[2, 1, 3, 3, 2, 1, 5], nums2=[2, 2]
输出：[2, 2]
"""


def get_intersection(array1, array2):
    # 对两个数组排序
    array1.sort()
    array2.sort()
    p1, p2 = 0, 0
    intersection = []
    while p1 < len(array1) and p2 < len(array2):
        if array1[p1] < array2[p2]:
            p1 += 1
        elif array1[p1] == array2[p2]:
            intersection.append(array1[p1])
            p1 += 1
            p2 += 1
        else:
            p2 += 1
    return intersection


if __name__ == "__main__":
    arr1 = [2, 1, 3, 3, 2, 1, 5]
    arr2 = [2, 2]
    print(get_intersection(arr1, arr2))
