"""
非递减数列：
    给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
    我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
示例 1:
    输入: nums = [4,2,3]
    输出: true
    解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:
    输入: nums = [4,2,1]
    输出: false
    解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

方法：
    1.遍历数组，并找到第一个当前元素比前一个元素大的索引i和前一个索引i-1；
    2.分别除去索引i和i-1的元素判断数组是否为递增，有一个递增说明满足改变一个元素的情况使数组变成非递减数组。
    时间复杂度为O(n)，空间复杂度为O(n)。
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        if len_nums <= 2:
            return True
        for i in range(1, len_nums):
            if nums[i] < nums[i - 1]:
                return self.checkExtendSortList(nums[:i] + nums[i+1:]) or self.checkExtendSortList(nums[:i-1] + nums[i:])
        return True

    def checkExtendSortList(self, nums: List[int]):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True
