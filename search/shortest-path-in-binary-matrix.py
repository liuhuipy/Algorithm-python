"""
二进制矩阵中的最短路径：
    在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。
    一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：
    * 相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
    * C_1 位于 (0, 0)（即，值为 grid[0][0]）
    * C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
    * 如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
    返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。
"""
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        elif n <= 2:
            return n
        temp = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        queue = [(0, 0, 1)]
        grid[0][0] = 1

        while queue:
            i, j, step = queue.pop(0)
            for a_x, a_y in temp:
                temp_x, temp_y = i + a_x, j + a_y
                if temp_x == n - 1 and temp_y == n - 1:
                    return step + 1
                if 0 <= temp_x < n and 0 <= temp_y < n and grid[temp_x][temp_y] == 0:
                    queue.append((temp_x, temp_y, step + 1))
                    grid[temp_x][temp_y] = 1

        return -1


# if __name__ == '__main__':
#     print(Solution().shortestPathBinaryMatrix(
#         [
#             [0, 0, 1, 0, 0, 0, 0],
#             [0, 1, 0, 0, 0, 0, 1],
#             [0, 0, 1, 0, 1, 0, 0],
#             [0, 0, 0, 1, 1, 1, 0],
#             [1, 0, 0, 1, 1, 0, 0],
#             [1, 1, 1, 1, 1, 0, 1],
#             [0, 0, 1, 0, 0, 0, 0]
#         ]
#     ))
