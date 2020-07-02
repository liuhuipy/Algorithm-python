"""
寻找重复数：
    给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
    假设只有一个重复的整数，找出这个重复的数。
示例 1:
    输入: [1,3,4,2,2]
    输出: 2
示例 2:
    输入: [3,1,3,4,2]
    输出: 3
说明：
    不能更改原数组（假设数组是只读的）。
    只能使用额外的 O(1) 的空间。
    时间复杂度小于 O(n2) 。
    数组中只有一个重复的数字，但它可能不止重复出现一次。

方法1：
    二分查找。
    时间复杂度为O(nlogn)，空间复杂度为O(1)。
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        len_nums = len(nums)
        left, right, mid = 1, len_nums - 1, 0
        while left < right:
            mid = (left + right) // 2
            cur = 0
            for num in nums:
                if num <= mid:
                    cur += 1
            if cur <= mid:
                left = mid + 1
            else:
                right = mid
        return left
