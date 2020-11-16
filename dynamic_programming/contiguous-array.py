"""
连续数组：
    给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）。
示例 1:
    输入: [0,1]
    输出: 2
    说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:
    输入: [0,1,0]
    输出: 2
    说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。

注意: 给定的二进制数组的长度不会超过50000。

方法：
    hashmap
"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        temp_map = dict()
        temp_map[0] = -1
        res, count = 0, 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in temp_map:
                res = max(res, i - temp_map[count])
            else:
                temp_map[count] = i
        return res
