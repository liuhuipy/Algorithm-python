"""
分割回文串：
    给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
    返回 s 所有可能的分割方案。

示例:
    输入: "aab"
    输出:
    [
        ["aa","b"],
        ["a","a","b"]
    ]
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        len_s = len(s)
        visited = set()

        def dfs(index, path):
            if index >= len_s:
                res.append(path)
                return
            for i in range(index, len_s):
                temp_s = s[index: i + 1]
                if temp_s in visited or self.check(temp_s):
                    visited.add(temp_s)
                    dfs(i + 1, path + [temp_s])

        dfs(0, [])
        return res

    def check(self, s):
        len_s = len(s)
        left, right = 0, len_s - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    print(Solution().partition("aabcba"))
