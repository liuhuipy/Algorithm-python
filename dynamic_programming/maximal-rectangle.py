"""
最大矩形：
    给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:
    输入:
    [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    输出: 6

"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        len_matrix = len(matrix)
        if not matrix:
            return 0
        len_row = len(matrix[0])
        res = 0
        dp = [0] * len_row
        for i in range(len_matrix):
            for j in range(len_row):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
            res = max(res, self.code_84(dp))
        return res

    @staticmethod
    def code_84(heights: List[int]):
        temp_stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while temp_stack[-1] != -1 and heights[temp_stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[temp_stack.pop()] * (i - temp_stack[-1] - 1))
            temp_stack.append(i)
        while temp_stack[-1] != -1:
            max_area = max(max_area, heights[temp_stack.pop()] * (len(heights) - temp_stack[-1] - 1))
        return max_area


if __name__ == '__main__':
    print(Solution().maximalRectangle(
        [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
        ]
    ))