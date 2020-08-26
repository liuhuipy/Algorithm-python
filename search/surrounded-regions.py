"""
被围绕的区域：
    给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
    找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:
    被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
    任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

方法：
    深度优先搜索。从矩阵四周边界开始进行dfs搜索值为'O'的元素记录到访问集合里面，然后遍历整个矩阵将未访问的且值为'O'的元素更新为'X'。
    时间复杂度为O(m * n)。
    空间复杂度为O(m * n)。
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        visited = set()
        len_col, len_row = len(board), len(board[0])

        def dfs_region(col, row):
            if (col, row) not in visited and 0 <= col < len_col and 0 <= row < len_row and board[col][row] == "O":
                visited.add((col, row))
                dfs_region(col + 1, row)
                dfs_region(col - 1, row)
                dfs_region(col, row + 1)
                dfs_region(col, row - 1)

        for i in range(len_col):
            dfs_region(i, 0)
            dfs_region(i, len_row - 1)

        for j in range(len_row):
            dfs_region(0, j)
            dfs_region(len_col - 1, j)

        for i in range(len_col):
            for j in range(len_row):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
