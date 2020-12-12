"""
冒泡排序

题目描述：使用冒泡排序对一个无序数组进行从小到大排序
输入：[1, 4, 9, 3, 5]
输出：[1, 3, 4, 5, 9]
"""


def bubble_sort(array):
    if len(array) <= 1:
        return array
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == "__main__":
    arr = [1, 4, 9, 3, 5]
    arr = bubble_sort(arr)
    print(arr)
