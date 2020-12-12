"""
题目描述：从有序数组中删除重复项
输入：[0, 0, 1, 1, 1, 2, 3, 4, 4]
输出：[0, 1, 2, 3, 4]
"""


def del_repeat(array):
    return set(array)
            

if __name__ == "__main__":
    arr = [0, 0, 1, 1, 1, 2, 3, 4, 4]
    print(del_repeat(arr))
