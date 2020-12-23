"""
存在重复

题目描述：判断数组中是否存在重复的元素
输入：[7, 1, 5, 3, 6, 4, 1]
输出：True
"""


def exist_repeat(array):
    if len(set(array)) != len(array):
        return True
    return False


if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4, 1]
    print(exist_repeat(arr))
