"""
有序数组中的单一元素：
    给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。
示例 1:
    输入: [1,1,2,3,3,4,4,8,8]
    输出: 2
示例 2:
    输入: [3,3,7,7,10,11,11]
    输出: 10
注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。。

方法1：
    遍历数组，找到出现次数只有一次的数。
    时间复杂度为O(n)，空间复杂度为O(1)。
方法2：
    二分查找。
    时间复杂度为O(logn)，空间复杂度为O(1)。
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            if nums[mid] == nums[mid - 1]:
                if (mid - l) % 2 != 0:
                    l = mid + 1
                else:
                    r = mid - 2
            else:
                if (r - mid) % 2 != 0:
                    r = mid - 1
                else:
                    l = mid + 2
        return nums[l]
