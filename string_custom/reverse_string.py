"""
反转字符串

题目描述：
输入：["h", "e", "l", "l", "o"]
输出：["o", "l", "l", "e", "h"]
"""


def reverse_string(array):
    if len(array) < 2:
        return
    for i in range(len(array)//2):
        array[i], array[len(array)-i-1] = array[len(array)-i-1], array[i]
    return array


if __name__ == "__main__":
    arr = ["h", "e", "l", "l", "o"]
    print(reverse_string(arr))
