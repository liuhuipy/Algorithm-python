"""
二维区域和检索-矩阵不可变：
    给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。
    上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

示例:
    给定 matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12
说明:
    你可以假设矩阵不可变。
    会多次调用 sumRegion 方法。
    你可以假设 row1 ≤ row2 且 col1 ≤ col2。

"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        if not n:
            return
        m = len(matrix[0])
        self.dp = [[0 for _ in range(m)] for _ in range(n)]
        self.dp[0][0] = matrix[0][0]
        for i in range(1, n):
            self.dp[i][0] = self.dp[i - 1][0] + matrix[i][0]
        for j in range(1, m):
            self.dp[0][j] = self.dp[0][j - 1] + matrix[0][j]
        for i in range(1, n):
            for j in range(1, m):
                self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            l_top_value, l_value, top_value = 0, 0, 0
        elif row1 == 0:
            l_top_value, l_value, top_value = 0, self.dp[row2][col1 - 1], 0
        elif col1 == 0:
            l_top_value, l_value, top_value = 0, 0, self.dp[row1 - 1][col2]
        else:
            l_top_value, l_value, top_value = self.dp[row1 - 1][col1 - 1], self.dp[row2][col1 - 1], self.dp[row1 - 1][col2]
        return self.dp[row2][col2] - l_value - top_value + l_top_value


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    param_1 = obj.sumRegion(1, 2, 2, 4)
    print(param_1)

