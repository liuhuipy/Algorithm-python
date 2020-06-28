"""
存在重复元素：
    给定一个整数数组，判断是否存在重复元素。如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
示例 1:
    输入: [1,2,3,1]
    输出: true
方法：
    哈希表法。
    时间复杂度为O(n)，空间复杂度为O(n)。
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp_dic = {}
        for num in nums:
            if num in temp_dic:
                return True
            temp_dic[num] = 1
        return False

