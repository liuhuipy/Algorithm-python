"""
合并两个有序数组：
    给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
说明:
    初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:
输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3
    输出: [1,2,2,3,5,6]
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left, right = 0, 0
        while left < m + right and right < n:
            if nums1[left] > nums2[right]:
                temp, left_index = nums2[right], left
                while left_index <= m + right:
                    current = nums1[left_index]
                    nums1[left_index], temp = temp, current
                    left_index += 1
                left += 1
                right += 1

            else:
                left += 1
        for i in range(right, n):
            nums1[left] = nums2[i]
            left += 1
