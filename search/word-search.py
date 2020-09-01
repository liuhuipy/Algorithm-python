"""
单词搜索：
    给定一个二维网格和一个单词，找出该单词是否存在于网格中。
    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
    board =
    [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    给定 word = "ABCCED", 返回 true
    给定 word = "SEE", 返回 true
    给定 word = "ABCB", 返回 false
提示：
    board 和 word 中只包含大写和小写英文字母。
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_board = len(board)
        len_board_child = len(board[0])
        len_word = len(word)
        temp_directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        temp_visited = [[0 for _ in range(len_board_child)] for _ in range(len_board)]

        def helper(col, row, index):
            if col < 0 or col >= len_board or row < 0 or row >= len_board_child or index >= len_word or \
                    board[col][row] != word[index] or temp_visited[col][row] == 1:
                return False
            if index == len_word - 1:
                return True

            temp_visited[col][row] = 1
            for x_add, y_add in temp_directs:
                if helper(col + x_add, row + y_add, index + 1):
                    return True
            temp_visited[col][row] = 0

        for i in range(len_board):
            for j in range(len_board_child):
                if helper(i, j, 0):
                    return True
        return False
