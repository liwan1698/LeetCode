"""
二分法查找

题目描述：使用二分法从有序数组中查找输入数字的位置
输入：数组为[1, 3, 4, 5, 9] 查找数字为4
输出：数字位置为2
"""

def binary_search(array, key):
    len_array = len(array)
    left = 0
    right = len_array - 1
    while right - left > 1:
        mid = (right + left) // 2  # //代表整数除法
        if key < array[mid]:
            right = mid
        elif key > array[mid]:
            left = mid
        else:
            return mid
    if key == array[left]:
        return left
    elif key == array[right]:
        return right
    else:
        return -1


if __name__ == "__main__":
    arr = [1, 3, 4, 5, 9]
    print(binary_search(arr, 9))
