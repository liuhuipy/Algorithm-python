"""
找两个和为目标值且不重叠的子数组：
    给你一个整数数组 arr 和一个整数值 target 。
    请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。
    请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。
示例 1：
    输入：arr = [3,2,2,4,3], target = 3
    输出：2
    解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。
示例 2：
    输入：arr = [7,3,4,7], target = 7
    输出：2
    解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。
示例 3：
    输入：arr = [4,3,2,6,2,3,4], target = 6
    输出：-1
    解释：我们只有一个和为 6 的子数组。
示例 4：
    输入：arr = [5,5,4,4,5], target = 3
    输出：-1
    解释：我们无法找到和为 3 的子数组。
示例 5：
    输入：arr = [3,1,1,1,5,1,2,1], target = 3
    输出：3
    解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。

提示：
    1 <= arr.length <= 10^5
    1 <= arr[i] <= 1000
    1 <= target <= 10^8

方法：
    滑动窗口+动态规划
"""
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left, window, res = 0, 0, n + 1
        dp = [n + 1] * n
        for i, num in enumerate(arr):
            window += num
            while window > target:
                window -= arr[left]
                left += 1
            if window == target:
                window_len = i - left + 1
                res = min(res, window_len + dp[left - 1])
                dp[i] = min(window_len, dp[i - 1])
            else:
                dp[i] = dp[i - 1]
        return res if res <= n else -1


if __name__ == '__main__':
    print(Solution().minSumOfLengths([3,1,1,1,5,1,2,1], 3))