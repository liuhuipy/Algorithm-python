"""
Pow(x,n)：
    实现 pow(x, n) ，即计算 x 的 n 次幂函数。
示例 1:
    输入: 2.00000, 10
    输出: 1024.00000
示例 2:
    输入: 2.10000, 3
    输出: 9.26100
示例 3:
    输入: 2.00000, -2
    输出: 0.25000
    解释: 2-2 = 1/22 = 1/4 = 0.25
说明:
    -100.0 < x < 100.0
    n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1]
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(N):
            res = 1.0
            x_contribute = x
            while N > 0:
                if N % 2 == 1:
                    res *= x_contribute
                x_contribute *= x_contribute
                N //= 2
            return res
        return helper(n) if n >= 0 else 1.0 / helper(-n)


if __name__ == '__main__':
    print(Solution().myPow(2, 10))