"""
长度最小的子数组：
    给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
    如果不存在符合条件的子数组，返回 0。
示例：
    输入：s = 7, nums = [2,3,1,2,4,3]
    输出：2
    解释：子数组 [4,3] 是该条件下的长度最小的子数组。
"""
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        ret, start, add_nums = n + 1, 0, 0
        for i in range(n):
            add_nums += nums[i]
            if add_nums < s:
                continue
            for j in range(start, i + 1):
                if add_nums >= s > add_nums - nums[j]:
                    ret = min(i - j + 1, ret)
                    start, add_nums = j + 1, add_nums - nums[j]
                    break
                add_nums -= nums[j]
        return ret if ret <= n else 0
