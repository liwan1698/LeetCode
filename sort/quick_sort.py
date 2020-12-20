"""
快速排序

题目描述：使用快速排序对一个无序数组进行从小到大排序
输入：[7, 1, 4, 9, 3, 5]
输出：[1, 3, 4, 5, 7, 9]
"""


def quick_sort(array):
    if len(array) <= 1:
        return array

    left = []
    right = []
    for i in array[1:]:
        if i <= array[0]:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [array[0]] + quick_sort(right)


if __name__ == "__main__":
    arr = [7, 1, 4, 9, 3, 5]
    print(quick_sort(arr))
