"""
乘积最大子数组：
    给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
示例 1:
    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6。
示例 2:
    输入: [-2,0,-1]
    输出: 0
    解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        min_num = max_num = res = nums[0]
        for num in nums[1:]:
            if max_num == 0:
                min_num, max_num = num, num
            else:
                min_num, max_num = min(min_num * num, max_num * num, num), max(min_num * num, max_num * num, num)
            res = max(max_num, res)
        return res


if __name__ == '__main__':
    print(Solution().maxProduct([2, 3, -2, 4, -1, 0, 2]))