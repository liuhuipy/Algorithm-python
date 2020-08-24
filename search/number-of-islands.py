"""
岛屿数量：
    给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
    此外，你可以假设该网格的四条边均被水包围。

示例 1:

输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1
示例 2:

输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def area_dfs(col, row):
            if col >= len_row or col < 0 or row < 0 or row >= len_col or grid[col][row] != "1":
                return
            grid[col][row] = "0"
            for c_x, c_y in term:
                area_dfs(col + c_x, row + c_y)

        len_row = len(grid)
        if not len_row or not grid[0]:
            return 0
        len_col = len(grid[0])
        res, temp = 0, 0
        term = ((0, -1), (0, 1), (1, 0), (-1, 0))
        for i in range(len_row):
            for j in range(len_col):
                if grid[i][j] == "1":
                    res += 1
                    area_dfs(i, j)
        return res
