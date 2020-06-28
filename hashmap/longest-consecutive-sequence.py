"""
最长连续序列：
    给定一个未排序的整数数组，找出最长连续序列的长度。
    要求算法的时间复杂度为 O(n)。
示例:
    输入: [100, 4, 200, 1, 3, 2]
    输出: 4
    解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
方法：
    利用哈希表，每次更新当前num左右最边连续的数目。
    时间复杂度为O(n)，空间复杂度为O(n)。
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp_dic = {}
        max_res = 0
        for num in nums:
            if num not in temp_dic:
                left = temp_dic.get(num - 1, 0)
                right = temp_dic.get(num + 1, 0)
                current_num = 1 + left + right
                max_res = max(current_num, max_res)
                temp_dic[num], temp_dic[num - left], temp_dic[num + right] = current_num, current_num, current_num
        return max_res

