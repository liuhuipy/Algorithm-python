"""
最长回文子串：
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。
示例 2：
    输入: "cbbd"
    输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l: int, r: int) -> str:
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return s[l + 1: r]

        n = len(s)
        res = ""
        for i in range(n):
            temp = helper(i - 1, i + 1)
            if len(res) < len(temp):
                res = temp
            if (i + 1) < n and s[i] == s[i + 1]:
                temp = helper(i - 1, i + 2)
                if len(res) < len(temp):
                    res = temp
        return res


if __name__ == '__main__':
    print(Solution().longestPalindrome("babadab"))