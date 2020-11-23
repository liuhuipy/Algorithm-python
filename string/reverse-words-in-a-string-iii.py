"""
反转字符串中的单词III：
    给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
示例：
    输入："Let's take LeetCode contest"
    输出："s'teL ekat edoCteeL tsetnoc"

提示：
    在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        n, start = len(s), -1
        res, temp = "", ""
        for i in range(n):
            if s[i] != " ":
                temp += s[i]
            elif temp:
                res += temp[::-1] + s[i]
                temp = ""
            else:
                res += s[i]
        res += temp[::-1]
        return res


if __name__ == '__main__':
    print(Solution().reverseWords("Let's take LeetCode contest"))