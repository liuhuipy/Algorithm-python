"""
回文数：
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
    输入: 121
    输出: true
示例 2:
    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

方法1：
    转换为字符串然后判断是否为回文串。
    时间复杂度为O(n)，空间复杂度为O(n)。
方法2：
    反转一半数字。
    时间复杂度为O(n)。空间复杂度为O(1)。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x > 0):
            return False
        temp_num = 0
        while x > temp_num:
            temp_num = temp_num * 10 + x % 10
            x = x // 10
        return x == temp_num or x == temp_num // 10

    def isPalindrome1(self, x: int) -> bool:
        temp_s = str(x)
        len_s = len(temp_s)
        left, right = 0, len_s - 1
        while left <= right:
            if temp_s[left] != temp_s[right]:
                return False
            left += 1
            right -= 1
        return True
