"""
最长上升子序列：
    给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
    输入: [10,9,2,5,3,7,101,18]
    输出: 4
    解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:
    可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
    你算法的时间复杂度应该为 O(n2) 。
    进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

方法1：
    动态规划。
    时间复杂度为O(n * n)，空间复杂度为O(n)。
方法2：
    动态规划。
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# if __name__ == '__main__':
#     print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
