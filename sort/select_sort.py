"""
选择排序

题目描述：使用选择排序对一个无序数组进行从小到大排序
输入：[1, 4, 9, 3, 5]
输出：[1, 3, 4, 5, 9]
"""


def select_sort(array):
    for i in range(0, len(array)-1):
        if array[i] > min(array[i:]):
            min_index = array.index(min(array[i:]))
            array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == "__main__":
    arr = [1, 4, 9, 3, 5]
    print(select_sort(arr))
