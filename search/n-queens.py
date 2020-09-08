"""
N皇后：
    给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
    每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例：
    输入：4
    输出：[
    [".Q..",  // 解法 1
     "...Q",
     "Q...",
     "..Q."],

    ["..Q.",  // 解法 2
     "Q...",
     "...Q",
     ".Q.."]
解释: 4 皇后问题存在两个不同的解法。
 
提示：
    皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = [-1] * n
        columns, diagonal1, diagonal2 = set(), set(), set()
        row = ["."] * n

        def build_board():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def dfs(row_n):
            if row_n == n:
                board = build_board()
                res.append(board)
            else:
                for i in range(n):
                    if i in columns or row_n - i in diagonal1 or row_n + i in diagonal2:
                        continue
                    queens[row_n] = i
                    columns.add(i)
                    diagonal1.add(row_n - i)
                    diagonal2.add(row_n + i)
                    dfs(row_n + 1)
                    columns.remove(i)
                    diagonal1.remove(row_n - i)
                    diagonal2.remove(row_n + i)
        dfs(0)
        return res
