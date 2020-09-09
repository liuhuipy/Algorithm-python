"""
完全平方数：
    给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:
    输入: n = 12
    输出: 3
    解释: 12 = 4 + 4 + 4.
示例 2:
    输入: n = 13
    输出: 2
    解释: 13 = 4 + 9.

方法：
    动态规划
"""


class Solution:
    def numSquares(self, n: int) -> int:
        x = self.computeSqrt(n)
        coins = [i * i for i in range(1, x + 1)]
        dp = [n + 1] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return -1 if dp[-1] == n + 1 else dp[-1]

    def computeSqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                l = mid + 1
            else:
                r = mid
        return l - 1 if x >= 2 else x

