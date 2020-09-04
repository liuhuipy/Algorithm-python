"""
解数独：
    编写一个程序，通过已填充的空格来解决数独问题。

    一个数独的解法需遵循如下规则：
        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

    空白格用 '.' 表示。

一个数独。
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],

答案被标成红色。
    ['5', '3', '4', '6', '7', '8', '9', '1', '2']
    ['6', '7', '2', '1', '9', '5', '3', '4', '8']
    ['1', '9', '8', '3', '4', '2', '5', '6', '7']
    ['8', '5', '9', '7', '6', '1', '4', '2', '3']
    ['4', '2', '6', '8', '5', '3', '7', '9', '1']
    ['7', '1', '3', '9', '2', '4', '8', '5', '6']
    ['9', '6', '1', '5', '3', '7', '2', '8', '4']
    ['2', '8', '7', '4', '1', '9', '6', '3', '5']
    ['3', '4', '5', '2', '8', '6', '1', '7', '9']
Note:
    给定的数独序列只包含数字 1-9 和字符 '.' 。
    你可以假设给定的数独只有唯一解。
    给定数独永远是 9x9 形式的。

方法：
    dfs（回溯）
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        len_board = 9
        temp_s_arr = [str(i + 1) for i in range(len_board)]
        col_map = {i: set() for i in range(len_board)}
        row_map = {i: set() for i in range(len_board)}
        area_map = {i + 1: set() for i in range(len_board)}
        for i in range(len_board):
            for j in range(len_board):
                board_s = board[i][j]
                if board_s != ".":
                    col_map[i].add(board_s)
                    row_map[j].add(board_s)
                    area_num = self.check_area(i, j)
                    area_map[area_num].add(board_s)

        def compute_index(col, row):
            if row == len_board - 1:
                col += 1
                row = 0
            else:
                row += 1
            return col, row

        def dfs(col, row):
            if col >= len_board or row >= len_board:
                return True

            if board[col][row] != ".":
                col, row = compute_index(col, row)
                return dfs(col, row)

            for temp_s in temp_s_arr:
                num = self.check_area(col, row)
                if temp_s in col_map[col] or temp_s in row_map[row] or temp_s in area_map[num]:
                    continue

                col_map[col].add(temp_s)
                row_map[row].add(temp_s)
                area_map[num].add(temp_s)
                board[col][row] = temp_s

                temp_col, temp_row = compute_index(col, row)
                if dfs(temp_col, temp_row):
                    return True

                col_map[col].remove(temp_s)
                row_map[row].remove(temp_s)
                area_map[num].remove(temp_s)
                board[col][row] = "."

            return False

        dfs(0, 0)
        return

    @staticmethod
    def check_area(col, row) -> int:
        return (col // 3) * 3 + row // 3 + 1


# if __name__ == '__main__':
#     board = [
#         ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#         [".", "9", "8", ".", ".", ".", ".", "6", "."],
#         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#         [".", "6", ".", ".", ".", ".", "2", "8", "."],
#         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#         [".", ".", ".", ".", "8", ".", ".", "7", "9"],
#     ]
#     print(Solution().solveSudoku(board))
