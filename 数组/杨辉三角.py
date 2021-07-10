"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
"""

row_num = 5
output = [
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
]


def gene_triple(num):
    ret = list()
    for i in range(num):
        row = list()
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(ret[i-1][j-1]+ret[i-1][j])
        ret.append(row)
    return ret


assert gene_triple(row_num) == output
