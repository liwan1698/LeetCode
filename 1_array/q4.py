"""
买卖股票最佳时机

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
输入：[7,1,5,3,6,4]
输出：5

题目分析：注意，题目只能买一次卖一次
"""


def max_profit(prices):
    min_price = 1e9
    max_profit = 0
    for price in prices:
        max_profit = max(price-min_price, max_profit)
        min_price = min(price, min_price)
    return max_profit


print(max_profit([7,1,5,3,6,4]))
