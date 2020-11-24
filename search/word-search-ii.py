"""
单词搜索II：
    给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
    单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
示例 1：
    输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    输出：["eat","oath"]
示例 2：
    输入：board = [["a","b"],["c","d"]], words = ["abcb"]
    输出：[]
提示：
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] 是一个小写英文字母
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] 由小写英文字母组成
    words 中的所有字符串互不相同

方法：
    前缀树+深度优先搜索
"""
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        m, n = len(board), len(board[0])
        res = []
        tern = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        trie = {}
        for word in words:
            t = trie
            for w in word:
                t = t.setdefault(w, {})
            t["end"] = 1

        def helper(i: int, j: int, s: str, use_trie) -> bool:
            c = board[i][j]
            if c not in use_trie:
                return
            use_trie = use_trie[c]
            if "end" in use_trie and use_trie["end"] == 1:
                res.append(s + c)
                use_trie["end"] = 0
                return

            board[i][j] = "#"
            for tran in tern:
                x, y = i + tran[0], j + tran[1]
                if 0 <= x < m and 0 <= y < n and board[x][y] != "#":
                    helper(i + tran[0], j + tran[1], s + c, use_trie)
            board[i][j] = c

        for i in range(m):
            for j in range(n):
                helper(i, j, "", trie)
        return res


if __name__ == '__main__':
    board = [["a","b"],["c","d"]]
    words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
    print(Solution().findWords(board, words))
