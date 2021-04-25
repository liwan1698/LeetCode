"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
"""


def find_triple_sum_zero(array):
    array.sort()
    output = []
    for fir in range(len(array)-2):
        if array[fir] > 0:  # 排序后的元素如果大于零，则后面的都大于零，全是正数后和不可能为零
            return output
        if fir > 0 and array[fir] == array[fir-1]:  # 如果元素相同，则结果已经包含到上一个元素的结果里，跳过
            continue
        for sec in range(fir+1, len(array)-1):
            thi = sec + 1
            if -array[fir] < array[sec] + array[thi]:   # 如果第二个和第三个元素的和已经大于第一个非正数的相反数，由于是排序后的数组，数组后面的数更大，所以跳出当前循环
                break
            while thi < len(array):
                if -array[fir] < array[sec] + array[thi]:
                    break
                elif -array[fir] > array[sec] + array[thi]: # 结果比较小则往后继续找
                    thi += 1
                else:
                    output.append([array[fir], array[sec], array[thi]])
                    break
    return output


print(find_triple_sum_zero([-1,0,1,2,-1,-4]))
