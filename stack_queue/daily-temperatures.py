"""
每日温度：
    请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，
    请在该位置用 0 来代替。
    例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

方法：
    使用单调栈从栈底到栈顶是递减的下标，每次遍历后维护这个单调栈。
"""
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        len_t = len(T)
        res, temp_stack = [0] * len_t, []
        for i in range(len_t - 1, -1, -1):
            while temp_stack:
                if T[temp_stack[-1]] > T[i]:
                    res[i] = temp_stack[-1] - i
                    break
                temp_stack.pop()
            temp_stack.append(i)
        return res
