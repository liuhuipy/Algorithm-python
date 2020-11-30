"""
最大整除子集：
    给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。
    如果有多个目标子集，返回其中任何一个均可。
示例 1:
    输入: [1,2,3]
    输出: [1,2] (当然, [1,3] 也正确)
示例 2:
    输入: [1,2,4,8]
    输出: [1,2,4,8]
"""
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [[num] for num in nums]
        res = [nums[0]]
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(res):
                res = dp[i]
        return res


if __name__ == '__main__':
    print(Solution().largestDivisibleSubset([1, 2, 3, 4, 6, 12]))