"""
实现strStr()：
    实现 strStr() 函数。
    给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
示例 1:
    输入: haystack = "hello", needle = "ll"
    输出: 2
示例 2:
    输入: haystack = "aaaaa", needle = "bba"
    输出: -1
说明:
    当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
    对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

方法：
    双指针
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        haystack_index, needle_index, hay_n, need_n = 0, 0, len(haystack), len(needle)
        while haystack_index < hay_n and needle_index < need_n:
            if haystack[haystack_index] == needle[needle_index]:
                if needle_index == need_n - 1:
                    return haystack_index - needle_index
                needle_index += 1
                haystack_index += 1
            elif needle_index > 0:
                haystack_index -= needle_index - 1
                needle_index = 0
            else:
                haystack_index += 1
        return -1


if __name__ == '__main__':
    print(Solution().strStr("mississipipi", "issipi"))