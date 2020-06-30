"""
错误的集合：
    集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，
    导致集合丢失了一个整数并且有一个元素重复。给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，
    再找到丢失的整数，将它们以数组的形式返回。
示例 1:
    输入: nums = [1,2,2,4]
    输出: [2,3]
方法：
    使用hashmap。
    时间复杂度为O(n)，空间复杂度为O(n)。
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp_dic = {i+1: 0 for i in range(len(nums))}
        for num in nums:
            temp_dic[num] += 1
        repeat_num, hiatus_num = 0, 0
        for i in range(1, len(nums) + 1):
            if temp_dic[i] == 0:
                hiatus_num = i
            elif temp_dic[i] > 1:
                repeat_num = i
        return [repeat_num, hiatus_num]
