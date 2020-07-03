"""
同构字符串：
    给定两个字符串 s 和 t，判断它们是否是同构的。
    如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
    所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
示例 1:
    输入: s = "egg", t = "add"
    输出: true
示例 2:
    输入: s = "foo", t = "bar"
    输出: false
示例 3:
    输入: s = "paper", t = "title"
    输出: true
说明:
    你可以假设 s 和 t 具有相同的长度。
方法：
    哈希表。
    时间复杂度为O(n)，空间复杂度为O(n)。
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic, len_s = {}, len(s)
        for i in range(len_s):
            if t[i] not in dic and s[i] not in dic.values():
                dic[t[i]] = s[i]
            elif t[i] not in dic or (t[i] in dic and dic[t[i]] != s[i]):
                return False
        return True
