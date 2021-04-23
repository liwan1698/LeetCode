"""
给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。
输入：nums = [555,901,482,1771]
输出：1
解释：
只有 1771 是位数为偶数的数字。
"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)

