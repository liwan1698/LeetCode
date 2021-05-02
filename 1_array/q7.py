"""
糖果棒交换

爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。
因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。
如果有多个答案，你可以返回其中任何一个。保证答案存在。

输入：A = [1,1], B = [2,2]
输出：[1,2]
输入：A = [2], B = [1,3]
输出：[2,3]
"""


def swap_sweet(sweet_A, sweet_B):
    sum_A = sum(sweet_A)
    sum_B = sum(sweet_B)
    delta = (sum_A - sum_B) // 2
    for j in sweet_B:
        i = j + delta
        if i in sweet_A:
            return [i, j]



print(swap_sweet([1,1], [2,2]))
print(swap_sweet([2], [1,3]))
