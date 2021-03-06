"""
最大连续1的个数：
    给定一个二进制数组， 计算其中最大连续1的个数。
示例 1:
    输入: [1,1,0,1,1,1]
    输出: 3
    解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, temp_num = 0, 0
        for num in nums:
            if num == 1:
                temp_num += 1
                res = max(res, temp_num)
            else:
                temp_num = 0
        return max(res, temp_num)
