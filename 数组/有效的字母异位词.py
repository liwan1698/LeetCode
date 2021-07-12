"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
"""

s1 = "anagram"
t1 = "nagaram"
output1 = True

s2 = "rat"
t2 = "car"
output2 = False


def is_valid(s, t):
    s_temp = list(s)
    s_temp.sort()
    s = ''.join(s_temp)
    t_temp = list(t)
    t_temp.sort()
    t = ''.join(t_temp)
    if s == t:
        return True
    return False


assert is_valid(s1, t1) == output1
assert is_valid(s2, t2) == output2
