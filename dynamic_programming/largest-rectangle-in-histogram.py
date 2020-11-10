"""
柱状图中最大的矩形：
    给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
    求在该柱状图中，能够勾勒出来的矩形的最大面积。
    以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
    图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
示例:
    输入: [2,1,5,6,2,3]
    输出: 10

方法：
    单调栈
    时间复杂度为O(n)。空间复杂度为O(n)
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        temp_stack = [-1]
        res = 0
        for i in range(n):
            while heights[temp_stack[-1]] > heights[i]:
                h = heights[temp_stack.pop()]
                w = i - temp_stack[-1] - 1
                res = max(res, h * w)
            temp_stack.append(i)
        heights.pop()
        return res


if __name__ == '__main__':
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
