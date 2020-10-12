"""
买卖股票的最佳时机：
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
    注意：你不能在买入股票前卖出股票。

示例 1:
    输入: [7,1,5,3,6,4]
    输出: 5
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
         注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:
    输入: [7,6,4,3,1]
    输出: 0
    解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

方法：
    动态规划。
    第i天最大利润为第i天卖出与前i-1天买入最低的价格只差，或者第i天不卖出（前i-1天已经我完成一次买卖），
    状态转移方程：dp[i] = max(dp[i - 1], prices[i] - min{[price[1], price[2], price[i-1]]})
    时间复杂度为O(n)。空间复杂度为O(1)。
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        m_num, res = prices[0], 0
        for price in prices:
            res = max(res, price - m_num)
            m_num = min(m_num, price)
        return res
