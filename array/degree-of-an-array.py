"""
数组的度：
    给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
    你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
示例 1:
    输入: [1, 2, 2, 3, 1]
    输出: 2
    解释:
    输入数组的度是2，因为元素1和2的出现频数最大，均为2.
    连续子数组里面拥有相同度的有如下所示:
        [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    最短连续子数组[2, 2]的长度为2，所以返回2.。
"""
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        temp_dic, len_nums, temp_max_count, temp_count_arr = {}, len(nums), 0, []
        for i in range(len_nums):
            num = nums[i]
            temp_dic.setdefault(num, [])
            temp_dic[num].append(i)

        for k, v in temp_dic.items():
            if len(v) > temp_max_count:
                temp_count_arr = [k]
                temp_max_count = len(v)
            elif len(v) == temp_max_count:
                temp_count_arr.append(k)
        res = len_nums
        for num in temp_count_arr:
            res = min(res, temp_dic[num][-1] - temp_dic[num][0] + 1)
        return res
