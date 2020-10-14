"""
最长连续递增序列：
    给定一个未经排序的整数数组，找到最长且连续的的递增序列，并返回该序列的长度。

示例 1:
    输入: [1,3,5,4,7]
    输出: 3
    解释: 最长连续递增序列是 [1,3,5], 长度为3。
    尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
示例 2:
    输入: [2,2,2,2,2]
    输出: 1
    解释: 最长连续递增序列是 [2], 长度为1。
"""
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res, temp_count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp_count += 1
                res = max(res, temp_count)
            else:
                temp_count = 1
        return res

