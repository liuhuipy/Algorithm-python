"""
岛屿的最大面积：
    给定一个包含了一些 0 和 1 的非空二维数组 grid 。
    一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
    你可以假设 grid 的四个边缘都被 0（代表水）包围着。
    找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:
    [[0,0,0,0,0,0,0,0]]
    对于上面这个给定的矩阵, 返回 0。

方法：
    深度优先搜索
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def area_dfs(col, row, area: int) -> int:
            if col >= len_row or col < 0 or row < 0 or row >= len_col or (col, row) in visited or grid[col][row] != 1:
                return 0
            visited.add((col, row))
            for c_x, c_y in term:
                area += area_dfs(col + c_x, row + c_y, 1)
            return area

        len_row = len(grid)
        if not len_row or not grid[0]:
            return 0
        len_col = len(grid[0])
        visited, res, temp = set(), 0, 0
        term = ((0, -1), (0, 1), (1, 0), (-1, 0))
        for i in range(len_row):
            for j in range(len_col):
                if (i, j) not in visited and grid[i][j] == 1:
                    ans = area_dfs(i, j, 1)
                    res = max(res, ans)
        return res


if __name__ == '__main__':
    print(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                      [0,1,1,0,1,0,0,0,0,0,0,0,0],
                                      [0,1,0,0,1,1,0,0,1,0,1,0,0],
                                      [0,1,0,0,1,1,0,0,1,1,1,0,0],
                                      [0,0,0,0,0,0,0,0,0,0,1,0,0],
                                      [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                      [0,0,0,0,0,0,0,1,1,0,0,0,0]]
                                     ))

