"""
递增子序列：
    给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:
    输入: [4, 6, 7, 7]
    输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:
    给定数组的长度不会超过15。
    数组中的整数范围是 [-100,100]。
    给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

方法1：
    动态规划：
    时间复杂度为O(n*n)，空间复杂度为O(n*n)。

方法2：
    DFS：todo
"""
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        len_nums = len(nums)
        dp = [[] for _ in range(len_nums)]
        dp[0] = [[nums[0]]]
        for i in range(1, len_nums):
            has_same = False
            for j in range(i - 1, -1, -1):
                if has_same:
                    break
                if nums[i] >= nums[j]:
                    for k in dp[j]:
                        dp[i].append(k + [nums[i]])
                        res.append(k + [nums[i]])

                if nums[i] == nums[j]:
                    has_same = True
            if not has_same:
                dp[i].append([nums[i]])
        return res


if __name__ == '__main__':
    print(Solution().findSubsequences([4, 6, 7, 7, 4]))
