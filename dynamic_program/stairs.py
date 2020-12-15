"""
爬楼梯

题目描述：
输入：阶梯数为5
输出：输出为8
"""


def get_step(n):
    need_step = [1, 1, 2]

    i = n
    while i > 2:
        need_step.append(need_step[-1] + need_step[-2])
        i -= 1
    return need_step[n]


if __name__ == "__main__":
    n = 5
    print(get_step(5))
