"""
零钱兑换：
    给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
    如果没有任何一种硬币组合能组成总金额，返回 -1。
    你可以认为每种硬币的数量是无限的。

示例 1：
    输入：coins = [1, 2, 5], amount = 11
    输出：3
    解释：11 = 5 + 5 + 1
示例 2：
    输入：coins = [2], amount = 3
    输出：-1
示例 3：
    输入：coins = [1], amount = 0
    输出：0
示例 4：
    输入：coins = [1], amount = 1
    输出：1
示例 5：
    输入：coins = [1], amount = 2
    输出：2

提示：
    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104

方法：
    动态规划：
    时间复杂度为O(m * amount)。空间复杂度为O(amount)。
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        len_coins = len(coins)
        for i in range(1, amount + 1):
            for j in range(len_coins):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return dp[-1] if dp[-1] != (amount + 1) else -1


if __name__ == '__main__':
    print(Solution().coinChange([1, 3, 5], 11))
