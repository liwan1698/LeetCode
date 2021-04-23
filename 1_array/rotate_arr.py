"""
旋转数组

题目描述：将数组中的元素向右移动k个位置
输入：[7, 1, 5, 3, 6, 4]， k=2
输出：[6, 4, 7, 1, 5, 3]
"""


def rotate(array, num):
    return array[len(array)-num:] + array[:len(array)-num]


if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    k = 2
    print(rotate(arr, k))
