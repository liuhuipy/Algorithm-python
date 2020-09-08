"""
组合总和II：
    给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的每个数字在每个组合中只能使用一次。
    说明：
        所有数字（包括目标数）都是正整数。
        解集不能包含重复的组合。 
示例 1:
    输入: candidates = [10,1,2,7,6,1,5], target = 8,
    所求解集为:
    [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6]
    ]
示例 2:
    输入: candidates = [2,5,2,1,2], target = 5,
    所求解集为:
    [
        [1,2,2],
        [5]
    ]

方法：
    dfs（回溯）
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        len_candidates = len(candidates)
        res = []

        def dfs(index, path, les_target):
            if not les_target:
                res.append(path)
                return
            for i in range(index, len_candidates):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > les_target:
                    break
                dfs(i + 1, path + [candidates[i]], les_target - candidates[i])
        dfs(0, [], target)
        return res