"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

def find_sum_equal_target(array, target):
    array.sort()
    all_ans = []
    def dfs(cur_arr, resid, ans):
        if resid == 0:
            all_ans.append(ans)
        if resid < 0:
            return
        i = 0
        n = len(cur_arr)
        while i < n:
            dfs(cur_arr[i+1:], resid-cur_arr[i], ans+[cur_arr[i]])
            j = i+1
            while j < n and cur_arr[i] == cur_arr[j]:
                j += 1
            i = j

    dfs(array, target, [])
    return all_ans


print(find_sum_equal_target([10,1,2,7,6,1,5], 8))
