"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""

prices1 = [7,1,5,3,6,4]
output1 = 5

prices2 = [7,6,4,3,1]
output2 = 0


def find_max_profit(prices):
    min_price = 1e9
    max_profit = 0
    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(price-min_price, max_profit)
    return max_profit


assert find_max_profit(prices1) == output1
assert find_max_profit(prices2) == output2

"""
题解：只需要保留最小的价格和当前最大的利润。下次自己再做不出来时可以用最笨的方法先做一遍。
"""
