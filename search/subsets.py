"""
子集：
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

方法1：
    dfs（回溯）
方法2：
    迭代
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        res = []

        def dfs(index, path, target):
            if not target:
                res.append(path)
                return
            if index >= len_nums:
                return
            for i in range(index, len_nums):
                dfs(i + 1, path + [nums[i]], target - 1)

        for child_len in range(0, len_nums + 1):
            dfs(0, [], child_len)
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [[i] + num for num in res]
        return res
