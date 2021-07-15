"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
"""

s1 = "()"
output1 = True

s2 = "()[]{}"
output2 = True

s3 = "(]"
output3 = False

s4 = "([)]"
output4 = False

s5 = "{[]}"
output5 = True


def is_valid(s):
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
            continue
        if stack[-1] == '(' and s[i] == ')':
            stack.pop(-1)
        elif stack[-1] == '{' and s[i] == '}':
            stack.pop(-1)
        elif stack[-1] == '[' and s[i] == ']':
            stack.pop(-1)
        else:
            stack.append(s[i])
    if len(stack) > 0:
        return False
    return True


assert is_valid(s1) == output1
assert is_valid(s2) == output2
assert is_valid(s3) == output3
assert is_valid(s4) == output4
assert is_valid(s5) == output5
