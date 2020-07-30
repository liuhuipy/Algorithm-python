"""
反转字符串中的元音字母：
    编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:
    输入: "hello"
    输出: "holle"
示例 2:
    输入: "leetcode"
    输出: "leotcede"
说明:
    元音字母不包含字母"y"。

"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        temp_set = set(("a", "A", "e", "E", "i", "I", "o", "O", "u", "U"))
        s_arr = list(s)
        left, right = 0, len(s_arr) - 1
        while left < right:
            if s_arr[left] not in temp_set:
                left += 1
            elif s_arr[right] not in temp_set:
                right -= 1
            else:
                s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
                left += 1
                right -= 1
        return "".join(s_arr)


# if __name__ == '__main__':
#     solution = Solution()
#     solution.reverseVowels("hello")
