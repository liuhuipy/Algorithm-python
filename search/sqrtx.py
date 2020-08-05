"""
x的平方根：
    实现 int sqrt(int x) 函数。
    计算并返回 x 的平方根，其中 x 是非负整数。
    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
示例 1:
    输入: 4
    输出: 2
示例 2:
    输入: 8
    输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            middle = (l + r) // 2
            c = middle * middle
            if c == x:
                return middle
            if c < x:
                l = middle + 1
            else:
                r = middle
        return l if l * l == x else l - 1
