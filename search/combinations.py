"""
组合：
    给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

方法：
    dfs（回溯）
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, visited = [], [False] * n

        def dfs(path, local_i):
            if len(path) == k:
                res.append(path)
                return
            if k - len(path) > n - local_i:
                return
            for i in range(local_i, n):
                if not visited[i]:
                    visited[i] = True
                    dfs(path + [i + 1], i)
                    visited[i] = False
        dfs([], 0)
        return res
