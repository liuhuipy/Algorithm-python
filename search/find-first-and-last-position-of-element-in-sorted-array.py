"""
在排序数组中查找元素的第一个和最后一个位置：
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。
    如果数组中不存在目标值，返回 [-1, -1]。
示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: [3,4]
示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: [-1,-1]
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        l, r = 0, len_nums
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                temp_l_index, temp_r_index = mid - 1, mid + 1
                while temp_l_index >= 0 and nums[temp_l_index] == target:
                    temp_l_index -= 1
                while temp_r_index < len_nums and nums[temp_r_index] == target:
                    temp_r_index += 1
                return [temp_l_index + 1, temp_r_index - 1]
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return [-1, -1]
