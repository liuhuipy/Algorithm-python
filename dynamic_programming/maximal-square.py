"""
最大正方形：
    在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
示例：
输入：
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
输出：4
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1 if matrix[i][j] == "1" else 0
                elif matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                res = max(res, dp[i][j])
        return res * res
