"""
有效的字母异位词：
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
示例 1:
    输入: s = "anagram", t = "nagaram"
    输出: true
示例 2:
    输入: s = "rat", t = "car"
    输出: false
说明：
    你可以假设字符串只包含小写字母。
方法：
    哈希表法。因字符串只包含小写字母，故map的键最多有26个，空间复杂度为O(1)。
    时间复杂度为O(n)，空间复杂度为O(1)。
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if len_s != len_t:
            return False
        dic = {}
        for i in range(len_s):
            dic.setdefault(s[i], 0)
            dic[s[i]] += 1
            dic.setdefault(t[i], 0)
            dic[t[i]] -= 1
        for _, v in dic.items():
            if v != 0:
                return False
        return True
