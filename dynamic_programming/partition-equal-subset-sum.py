"""
分割等和子集：
    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:
    每个数组中的元素不会超过 100
    数组的大小不会超过 200
示例 1:
    输入: [1, 5, 11, 5]
    输出: true
    解释: 数组可以分割成 [1, 5, 5] 和 [11].
示例 2:
    输入: [1, 2, 3, 5]
    输出: false
    解释: 数组不能分割成两个元素和相等的子集.。

方法：
    动态规划。
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 != 0:
            return False
        half_sum = num_sum // 2
        dp = [True] * (half_sum + 1)
        for num in nums:
            temp_num = half_sum - num
            if temp_num < 0:
                return False
            if temp_num == 0 or not dp[temp_num]:
                return True

            for i in range(half_sum, 0, -1):
                if dp[i] and i > num:
                    dp[i] = dp[i - num]
            dp[num] = False

        return False
