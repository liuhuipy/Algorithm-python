"""
转换成小写字母：
    实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
示例 1：
    输入: "Hello"
    输出: "hello"
示例 2：
    输入: "here"
    输出: "here"
示例 3：
    输入: "LOVELY"
    输出: "lovely"

"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            ascii_num = ord(s[i])
            if 65 <= ascii_num <= 90:
                res += chr(ascii_num + 32)
            else:
                res += s[i]
        return res


if __name__ == '__main__':
    print(Solution().toLowerCase("HeaD"))