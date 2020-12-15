"""
插入排序

题目描述：使用插入排序对一个无序数组进行从小到大排序
输入：[1, 4, 9, 3, 5]
输出：[1, 3, 4, 5, 9]
"""


def insert_sort(array):
    for right in range(1, len(array)):
        for left in range(0, right):
            target = array[right]
            if target < array[left]:
                array[left+1:right+1] = array[left:right]
                array[left] = target
                break
    return array


if __name__ == "__main__":
    arr = [1, 4, 9, 3, 5]
    print(insert_sort(arr))
