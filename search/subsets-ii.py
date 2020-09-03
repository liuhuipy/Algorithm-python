"""
子集II：
    给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

方法：
    dfs（回溯）
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        len_nums = len(nums)
        res = []

        def dfs(index, path, target):
            if not target:
                res.append(path)
                return
            if index >= len_nums:
                return
            for i in range(index, len_nums):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, path + [nums[i]], target - 1)

        for child_len in range(len_nums + 1):
            dfs(0, [], child_len)
        return res
