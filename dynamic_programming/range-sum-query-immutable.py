"""
区域和检索-数组不可变：
    给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

说明:
    你可以假设数组不可变。
    会多次调用 sumRange 方法。

方法：
    动态规划。初始化一个数组计算当前位置的和。
    时间复杂度为O(1)，空间复杂度为O(n)。
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = nums[:]
        for i in range(1, len(nums)):
            self.dp[i] += self.dp[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i - 1] if i > 0 else self.dp[j]
