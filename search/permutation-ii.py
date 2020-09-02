"""
全排列II：
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

方法：
    dfs（回溯）
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        len_nums = len(nums)
        res, visited = [], [False] * len_nums

        def dfs(path):
            if len(path) == len_nums:
                res.append(path)
                return
            for i in range(len_nums):
                if not visited[i]:
                    if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
                        continue
                    visited[i] = True
                    dfs(path + [nums[i]])
                    visited[i] = False

        dfs([])
        return res


# if __name__ == '__main__':
#     print(Solution().permuteUnique([1, 2, 1]))
