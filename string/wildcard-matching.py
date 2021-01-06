"""
通配符匹配：
    给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。
    两个字符串完全匹配才算匹配成功。
    说明:
        s 可能为空，且只包含从 a-z 的小写字母。
        p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:
    输入:
    s = "aa"
    p = "a"
    输出: false
    解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:
    输入:
    s = "aa"
    p = "*"
    输出: true
    解释: '*' 可以匹配任意字符串。
示例 3:
    输入:
    s = "cb"
    p = "?a"
    输出: false
    解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:
    输入:
    s = "adceb"
    p = "*a*b"
    输出: true
    解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:
    输入:
    s = "acdcb"
    p = "a*c?b"
    输出: false
方法1：
    动态规划
    时间复杂度为O(m*n)，空间复杂度为O(m*n)。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        dp = [[False for _ in range(np + 1)] for _ in range(ns + 1)]
        dp[0][0] = True
        for j in range(1, np + 1):
            if p[j - 1] != "*":
                break
            dp[0][j] = dp[0][j - 1]
        for i in range(1, ns + 1):
            for j in range(1, np + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    s = "cb"
    p = "*a"
    print(Solution().isMatch(s, p))
