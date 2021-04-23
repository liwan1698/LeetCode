"""
获得股票的最大收益

题目描述：输入是每天的股价，经可能完成多次交易。不能同时参与多笔交易，购买前必须卖掉之前所有的股票
输入：[7, 1, 5, 3, 6, 4]
输出：7
"""


def max_profit(array):
    profit = 0
    i = 1
    while i < len(array):
        if array[i] > array[i-1]:
            profit += array[i] - array[i-1]
        i += 1

    return profit


if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    print(max_profit(arr))
