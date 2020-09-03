"""
组合总和III：
    找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
    说明：
        所有数字都是正整数。
        解集不能包含重复的组合。 
示例 1:
    输入: k = 3, n = 7
    输出: [[1,2,4]]
示例 2:
    输入: k = 3, n = 9
    输出: [[1,2,6], [1,3,5], [2,3,4]]
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        len_nums = len(nums)
        res = []

        def dfs(index, path, les_target):
            if not les_target and len(path) == k:
                res.append(path[:])
                return
            if not les_target or len(path) > k:
                return

            for i in range(index, len_nums):
                if nums[i] > les_target:
                    break
                path.append(nums[i])
                dfs(i + 1, path, les_target - nums[i])
                path.pop()

        dfs(0, [], n)
        return res
