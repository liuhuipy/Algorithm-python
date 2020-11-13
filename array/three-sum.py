"""
三数之和：
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
    注意：答案中不可以包含重复的三元组。

示例：
    给定数组 nums = [-1, 0, 1, 2, -1, -4]，
    满足要求的三元组集合为：
    [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
方法：
    双指针
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                if (nums[left] + nums[right] + nums[i]) == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif (nums[left] + nums[right] + nums[i]) < 0:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))