"""
打家劫舍II：
    你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
    同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
    输入: [2,3,2]
    输出: 3
    解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:
    输入: [1,2,3,1]
    输出: 4
    解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
         偷窃到的最高金额 = 1 + 3 = 4 。

方法：
    动态规划：分别计算偷取1号房间和不偷取1号房间的最高偷窃金额，然后取较大值。
    时间复杂度为O(n)。空间复杂度为O(n)。
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums = len(nums)

        def compute_sums(robber_nums):
            left, right = 0, 0
            for num in robber_nums:
                left, right = right, max(right, left + num)
            return right

        return 0 if len_nums == 0 else nums[0] if len_nums == 1 else max(
            compute_sums(nums[1:]), compute_sums(nums[: len_nums - 1])
        )
