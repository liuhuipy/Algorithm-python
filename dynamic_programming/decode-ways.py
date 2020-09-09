"""
解码方法：
    一条包含字母 A-Z 的消息通过以下方式进行了编码：
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:
    输入: "12"
    输出: 2
    解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:
    输入: "226"
    输出: 3
    解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

方法：
    动态规划。
    时间复杂度为O(n)。空间复杂度为O(1)。
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        un_choice, choice = 1, 1
        for i in range(1, len(s)):
            if (s[i] == "0" and s[i - 1] == "0") or (s[i] == "0" and int(s[i - 1] + s[i]) > 26):
                return 0
            if s[i] == "0":
                choice = un_choice
            else:
                temp = un_choice
                un_choice = choice
                if s[i - 1] != "0":
                    choice = choice + temp if int(s[i - 1] + s[i]) <= 26 else choice
        return choice


if __name__ == '__main__':
    print(Solution().numDecodings("226"))
