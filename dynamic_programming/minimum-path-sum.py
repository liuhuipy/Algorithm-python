"""
最小路径和：
    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
    说明：每次只能向下或者向右移动一步。

示例:
    输入:
    [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。

方法：
    动态规划。
    时间复杂度为O(m * n)。空间复杂度为O(1)。
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_grid = len(grid)
        if not len_grid:
            return 0
        len_child_grid = len(grid[0])

        for i in range(len_grid):
            for j in range(len_child_grid):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])

        return grid[-1][-1]

