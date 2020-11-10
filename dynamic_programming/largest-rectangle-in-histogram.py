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
        n = len(heights)
        left, right = [0] * n, [0] * n
        temp_stack = []
        for i in range(n):
            while temp_stack and heights[temp_stack[-1]] >= heights[i]:
                temp_stack.pop()
            left[i] = temp_stack[-1] if temp_stack else -1
            temp_stack.append(i)
        temp_stack = []
        for i in range(n - 1, -1, -1):
            while temp_stack and heights[temp_stack[-1]] >= heights[i]:
                temp_stack.pop()
            right[i] = temp_stack[-1] if temp_stack else n
            temp_stack.append(i)

        res = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return res


if __name__ == '__main__':
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
