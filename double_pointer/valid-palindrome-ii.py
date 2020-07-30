"""
验证回文字符串II：
    给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:
    输入: "aba"
    输出: True
示例 2:
    输入: "abca"
    输出: True
    解释: 你可以删除c字符。

注意:
    字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(left, right, has_del):
            while left < right:
                if s[left] != s[right]:
                    if has_del:
                        return False
                    return valid(left + 1, right, True) or valid(left, right - 1, True)
                left += 1
                right -= 1
            return True

        left, right, has_del = 0, len(s) - 1, False
        return valid(left, right, has_del)
