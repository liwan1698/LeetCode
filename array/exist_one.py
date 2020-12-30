"""
只出现一次的数字

题目描述：判断数组中是否存在只出现一次的数字,如果有则返回，没有则返回0
输入：[2, 1, 3, 3, 2, 1, 5]
输出：True
"""


def exist_one(array):
    one_num = 0
    for i in array:
        one_num ^= i
    return one_num


if __name__ == "__main__":
    arr = [2, 1, 3, 3, 2, 1, 5]
    print(exist_one(arr))
