"""
太平洋大西洋水流问题：
    给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
    规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
    请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

提示：
输出坐标的顺序不重要
m 和 n 都小于150

示例：
给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:
    [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).

方法：
    深度优先搜索。
"""
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        len_col, len_row = len(matrix), len(matrix[0])
        visited_t_flow = set()
        visited_d_flow = set()

        def dfs_atlantic_water(col: int, row: int, child_val: int, t_water: bool):
            if (t_water and (col, row) in visited_t_flow) or (not t_water and (col, row) in visited_d_flow):
                return
            if 0 <= col < len_col and 0 <= row < len_row and matrix[col][row] >= child_val:
                if t_water:
                    visited_t_flow.add((col, row))
                else:
                    visited_d_flow.add((col, row))
                dfs_atlantic_water(col + 1, row, matrix[col][row], t_water)
                dfs_atlantic_water(col - 1, row, matrix[col][row], t_water)
                dfs_atlantic_water(col, row + 1, matrix[col][row], t_water)
                dfs_atlantic_water(col, row - 1, matrix[col][row], t_water)

        for i in range(len_col):
            dfs_atlantic_water(i, 0, 0, True)
            dfs_atlantic_water(i, len_row - 1, 0, False)

        for j in range(len_row):
            dfs_atlantic_water(0, j, 0, True)
            dfs_atlantic_water(len_col - 1, j, 0, False)

        res = []
        for t_col, t_row in visited_t_flow:
            if (t_col, t_row) in visited_d_flow:
                res.append([t_col, t_row])
        return res


# if __name__ == '__main__':
#     matrix = [
#         [1, 2, 2, 3, 5],
#         [3, 2, 3, 4, 4],
#         [2, 4, 5, 3, 1],
#         [6, 7, 1, 4, 5],
#         [5, 1, 1, 2, 4],
#     ]
#     print(Solution().pacificAtlantic(matrix))
