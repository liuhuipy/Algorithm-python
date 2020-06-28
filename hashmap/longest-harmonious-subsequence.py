"""
最长和谐子序列：
    和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
示例 1:
    输入: [1,3,2,2,5,2,3,7]
    输出: 5
    原因: 最长的和谐数组是：[3,2,2,2,3].
方法1：
    哈希表记录数组中每个值的数量，再遍历哈希表获取差为1的数目。
"""
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        temp_dic = {}
        for num in nums:
            temp_dic.setdefault(num, 0)
            temp_dic[num] += 1
        res = 0
        for k, v in temp_dic.items():
            if k + 1 in temp_dic:
                res = max(res, v + temp_dic[k + 1])
        return res
