"""
最长有效括号：
    给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
示例 1:
    输入: "(()"
    输出: 2
    解释: 最长有效括号子串为 "()"
示例 2:
    输入: ")()())"
    输出: 4
    解释: 最长有效括号子串为 "()()"
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        stack = []
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif stack:
                p = stack.pop()
                dp[i + 1] = dp[p] + i - p + 1
        return max(dp)


if __name__ == '__main__':
    print(Solution().longestValidParentheses("(())()"))