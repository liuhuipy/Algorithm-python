"""
旋转数组：
    给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
    输入: [1,2,3,4,5,6,7] 和 k = 3
    输出: [5,6,7,1,2,3,4]
解释:
    向右旋转 1 步: [7,1,2,3,4,5,6]
    向右旋转 2 步: [6,7,1,2,3,4,5]
    向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:
    输入: [-1,-100,3,99] 和 k = 2
    输出: [3,99,-1,-100]
解释:
    向右旋转 1 步: [99,-1,-100,3]
    向右旋转 2 步: [3,99,-1,-100]
说明:
    尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    要求使用空间复杂度为 O(1) 的 原地 算法。

方法1：
    使用中间数组存放移动后的值。
    时间复杂度为O(n)。
    空间复杂度为O(n)。
方法2：
    环状替换。
    时间复杂度为O(n)。
    空间复杂度为O(1)。
方法3：
    数组翻转。
    时间复杂度为O(n)。
    空间复杂度为O(1)。
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        temp_arr = [0] * len_nums
        for i in range(len_nums):
            temp_arr[(i + k) % len_nums] = nums[i]
        for i in range(len_nums):
            nums[i] = temp_arr[i]

    def rotate2(self, nums: List[int], k: int) -> None:
        if not nums or k < 1:
            return
        n = len(nums)
        start = temp = i = 0
        temp_val = nums[temp]
        while i < n:
            new_index = (temp + k) % n
            temp, temp_val, nums[new_index] = new_index, nums[new_index], temp_val
            if temp == start and i < n - 1:
                start += 1
                temp = start
                temp_val = nums[temp]
            i += 1

    def rotate3(self, nums: List[int], k: int) -> None:
        def swap(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        k %= n
        swap(0, n - 1)
        swap(0, k - 1)
        swap(k, n - 1)