"""
回文子串：
    给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
    具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
示例 1:
    输入: "abc"
    输出: 3
    解释: 三个回文子串: "a", "b", "c".
示例 2:
    输入: "aaa"
    输出: 6
    说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:
    输入的字符串长度不会超过1000。
方法：
    定一个回文串的中间元素，然后用左右指针寻更长的回文串。
    时间复杂度为O(n*n)，空间复杂度为O(1)
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        len_s = len(s)
        for i in range(len_s):
            res += 1
            left, right = i - 1, i + 1
            while left >= 0 and right < len_s:
                if s[left] != s[right]:
                    break
                res += 1
                left -= 1
                right += 1

            if i + 1 < len_s and s[i] == s[i + 1]:
                res += 1
                left, right = i - 1, i + 2
                while left >= 0 and right < len_s:
                    if s[left] != s[right]:
                        break
                    res += 1
                    left -= 1
                    right += 1
        return res
