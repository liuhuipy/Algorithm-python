"""
最长递增子序列的个数：
    给定一个未排序的整数数组，找到最长递增子序列的个数。
示例 1:
    输入: [1,3,5,4,7]
    输出: 2
    解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:
    输入: [2,2,2,2,2]
    输出: 5
    解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
    注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        len_arr = [1] * n
        count_arr = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    local_len = len_arr[j] + 1
                    if local_len > len_arr[i]:
                        len_arr[i], count_arr[i] = local_len, count_arr[j]
                    elif local_len == len_arr[i]:
                        count_arr[i] += count_arr[j]
        res_len = max(len_arr)
        return sum(c for i, c in enumerate(count_arr) if len_arr[i] == res_len)


if __name__ == '__main__':
    print(Solution().findNumberOfLIS([1,1,1,2,2,2,3,3,3]))



