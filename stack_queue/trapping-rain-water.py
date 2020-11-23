"""
接雨水：
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：
    输入：height = [4,2,0,3,2,5]
    输出：9
提示：
    n == height.length
    0 <= n <= 3 * 104
    0 <= height[i] <= 105

方法1：
    算出每个位置左边和右边最高的值，分别计算每个位置能装的水。
    时间复杂度为O(n)。空间复杂度为O(n)。
方法2：
    双指针。
    时间复杂度为O(n)。空间复杂度为O(1)。
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res, n = 0, len(height)
        left, right = 0, n - 1
        left_max, right_max = height[0], height[n - 1]
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res

    def trap_1(self, height: List[int]) -> int:
        if not height:
            return 0
        res, n = 0, len(height)
        left_max, right_max = [0] * n, [0] * n
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res


if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
