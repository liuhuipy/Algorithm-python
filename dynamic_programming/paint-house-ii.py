"""
粉刷房子II：
    假如有一排房子，共 n 个，每个房子可以被粉刷成 k 种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
    当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x k 的矩阵来表示的。
    例如，costs[0][0] 表示第 0 号房子粉刷成 0 号颜色的成本花费；costs[1][2] 表示第 1 号房子粉刷成 2 号颜色的成本花费，以此类推。
    请你计算出粉刷完所有房子最少的花费成本。

注意：
    所有花费均为正整数。

示例：
    输入: [[1,5,3],[2,9,4]]
    输出: 5
    解释: 将 0 号房子粉刷成 0 号颜色，1 号房子粉刷成 2 号颜色。最少花费: 1 + 4 = 5;
         或者将 0 号房子粉刷成 2 号颜色，1 号房子粉刷成 0 号颜色。最少花费: 3 + 2 = 5.
进阶：
    您能否在 O(nk) 的时间复杂度下解决此问题？

方法：
    动态规划：
    时间复杂度为O(nk)，空间复杂度为O(n)
"""
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        len_costs = len(costs)
        len_k = len(costs[0])
        dp = [[0, 0] for _ in range(len_costs)]
        first_m, second_m = 0, 0

        for i in range(len_costs):
            temp_f, temp_s = first_m, second_m
            first_m, second_m = float("inf"), float("inf")
            for j in range(len_k):
                if i == 0:
                    temp = temp_f + costs[i][j]
                elif j == dp[i - 1][0]:
                    temp = temp_s + costs[i][j]
                else:
                    temp = temp_f + costs[i][j]

                if temp <= first_m:
                    dp[i][0], dp[i][1] = j, dp[0][0]
                    first_m, second_m = temp, first_m
                elif first_m < temp <= second_m:
                    dp[i][1] = j
                    second_m = temp
        return first_m


# if __name__ == '__main__':
#     print(Solution().minCostII(
#         [
#             [3,20,7,7,16,8,7,12,11,19,1],
#             [10,14,3,3,9,13,4,12,14,13,1],
#             [10,1,14,11,1,16,2,7,16,7,19],
#             [13,20,17,15,3,13,8,10,7,8,9],
#             [4,14,18,15,11,9,19,3,15,12,15],
#             [14,12,16,19,2,12,13,3,11,10,9],
#             [18,12,10,16,19,9,18,4,14,2,4]
#         ]
#     ))
