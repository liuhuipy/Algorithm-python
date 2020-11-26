"""
最长等差数列：
    给定一个整数数组 A，返回 A 中最长等差子序列的长度。
    回想一下，A 的子序列是列表 A[i_1], A[i_2], ..., A[i_k] 其中 0 <= i_1 < i_2 < ... < i_k <= A.length - 1。
    并且如果 B[i+1] - B[i]( 0 <= i < B.length - 1) 的值都相同，那么序列 B 是等差的。
示例 1：
    输入：[3,6,9,12]
    输出：4
    解释：
    整个数组是公差为 3 的等差数列。
示例 2：
    输入：[9,4,7,2,10]
    输出：3
    解释：
    最长的等差子序列是 [4,7,10]。
示例 3：
    输入：[20,1,15,3,10,5,8]
    输出：4
    解释：
    最长的等差子序列是 [20,15,10,5]。
提示：
    2 <= A.length <= 2000
    0 <= A[i] <= 10000

"""
from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [{} for _ in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(i):
                cha = A[i] - A[j]
                dp[i][cha] = dp[j][cha] + 1 if cha in dp[j] else 2
                res = max(res, dp[i][cha])
        return res


if __name__ == '__main__':
    print(Solution().longestArithSeqLength([9,4,7,2,10]))
