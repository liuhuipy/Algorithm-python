"""
平方数之和：
    给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:
    输入: 5
    输出: True
    解释: 1 * 1 + 2 * 2 = 5

示例2:
    输入: 3
    输出: False
"""
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            temp = left * left + right * right
            if temp == c:
                return True
            if temp < c:
                left += 1
            else:
                right -= 1
        return False


# if __name__ == '__main__':
#     solution = Solution()
#     print(solution.judgeSquareSum(100000000))
