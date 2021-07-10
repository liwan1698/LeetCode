"""
在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
"""

nums1 =[[1,2], [3,4]]
r1 = 4
c1 = 1
output1 = [[1],[2],[3],[4]]

nums2 =[[1,2], [3,4]]
r2 = 2
c2 = 4
output2 = [[1,2],[3,4]]


def reshape_matrix(mat, r, c):
    m, n = len(mat), len(mat[0])
    if r*c != m*n:
        return mat
    new_mat = [[0]*c for _ in range(r)]
    for i in range(r*c):
        new_mat[i//c][i%c] = mat[i//n][i%n]
    return new_mat


assert reshape_matrix(nums1, r1, c1) == output1
assert reshape_matrix(nums2, r2, c2) == output2
