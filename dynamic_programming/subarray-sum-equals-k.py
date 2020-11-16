"""
和为K的子数组：
    给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
示例 1 :
    输入:nums = [1,1,1], k = 2
    输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
    说明 :
        数组的长度为 [1, 20,000]。
    数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        temp_map = dict()
        temp_map[0] = 1
        count, res = 0, 0
        for i in range(len(nums)):
            count += nums[i]
            if (count - k) in temp_map:
                res += temp_map[count - k]
            temp_map[count] = temp_map.get(count, 0) + 1
        return res


if __name__ == '__main__':
    print(Solution().subarraySum([1, 1, -1, 1], 2))