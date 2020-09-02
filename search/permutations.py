"""
全排列：
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

方法1：
    dfs（回溯）
方法2：
    见缝插数
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(temp_nums, path):
            if not temp_nums:
                res.append(path)
                return
            for i in range(len(temp_nums)):
                dfs(temp_nums[:i] + temp_nums[i + 1:], path + [temp_nums[i]])

        dfs(nums, [])
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [num] + perm[i:])
            perms = new_perms
        return perms


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
