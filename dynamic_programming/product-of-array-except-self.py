"""
除自身之外数组的乘积：
    给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
示例:
    输入: [1,2,3,4]
    输出: [24,12,8,6]
    提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
    说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
进阶：
    你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1] * (n + 1)
        zero_num = []
        for i in range(n):
            if nums[i] == 0:
                zero_num.append(i)
            dp[i + 1] = dp[i] * nums[i]
        res = [0] * n
        if len(zero_num) >= 2:
            return res
        if len(zero_num) == 1:
            zero_index = zero_num[0]
            left_num = dp[zero_index]
            for i in range(zero_index + 1, n):
                left_num *= nums[i]
            res[zero_index] = left_num
            return res
        for i in range(n):
            res[i] = dp[n] // nums[i]
        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf([-3,1,0, 4]))