"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""

s1 = "leetcode"
output1 = 0

s2 = "loveleetcode"
output2 = 2


def find_first_only_char(s):
    for i in range(len(s)):
        if s[i] not in s[:i] and s[i] not in s[i+1:]:
            return i
    return -1


assert find_first_only_char(s1) == output1
assert find_first_only_char(s2) == output2
