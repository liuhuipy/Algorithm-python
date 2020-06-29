"""
重塑矩阵：
    在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
    给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
    重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
    如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
示例 1:
    输入:
        nums =
        [
            [1, 2],
            [3, 4]
        ]
        r = 1, c = 4
    输出:
        [[1, 2, 3, 4]]
解释:
    行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。

"""
from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums:
            return nums
        len_nums, len_col = len(nums), len(nums[0])
        if len_nums * len_col != r * c:
            return nums

        temp_l, temp_arr, res = 0, [], []
        for i in range(len_nums):
            for j in range(len_col):
                temp_l += 1
                temp_arr.append(nums[i][j])
                if temp_l == c:
                    res.append(temp_arr)
                    temp_l, temp_arr = 0, []
        return res
