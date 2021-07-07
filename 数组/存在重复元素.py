"""
给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
"""

# 解法1
def is_repeat1(arr):
    if len(set(arr)) < len(arr):
        return True
    return False


# 解法2
def is_repeat(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    return False


arr1 = [1, 2, 3, 1]
arr2 = [1, 2, 3, 4]
arr3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

assert is_repeat(arr1) == True
assert is_repeat(arr2) == False
assert is_repeat(arr3) == True


"""
题解：此题考察的是排序，如果出现数组，可直接考虑上三板斧-排序
"""
