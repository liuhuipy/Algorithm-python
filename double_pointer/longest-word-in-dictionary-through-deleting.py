"""
通过删除字母匹配到字典里最长单词：
    给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。
    如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

示例 1:
输入:
    s = "abpcplea", d = ["ale","apple","monkey","plea"]
输出:
    "apple"

示例 2:
输入:
    s = "abpcplea", d = ["a","b","c"]
输出:
    "a"
说明:
    所有输入的字符串只包含小写字母。
    字典的大小不会超过 1000。
    所有输入的字符串长度不会超过 1000。

"""
from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res, temp_len, len_s = "", 0, len(s)
        for dd in d:
            left, right = 0, 0
            len_dd = len(dd)
            while left < len_s and right < len_dd:
                if s[left] == dd[right]:
                    left += 1
                    right += 1
                else:
                    left += 1
            if right == len_dd:
                if len_dd > temp_len:
                    temp_len, res = len_dd, dd
                elif len_dd == temp_len:
                    res = min(res, dd)
        return res
