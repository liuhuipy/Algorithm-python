"""
一和零：
    在计算机界中，我们总是追求用有限的资源获取最大的收益。
    现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
    你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。

示例 1:
    输入: strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
    输出: 4
    解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
示例 2:
    输入: strs = ["10", "0", "1"], m = 1, n = 1
    输出: 2
    解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。

提示：
    1 <= strs.length <= 600
    1 <= strs[i].length <= 100
    strs[i] 仅由 '0' 和 '1' 组成
    1 <= m, n <= 100

方法：
    动态规划：
    时间复杂度为O(m*n*l)。空间复杂度为O(m*n)。
"""
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs:
            return 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            one_num, zero_num = self.compute_s(s)
            for i in range(m, zero_num - 1, -1):
                for j in range(n, one_num - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero_num][j - one_num] + 1)
        return dp[m][n]

    @staticmethod
    def compute_s(child_s) -> (int, int):
        one_num, zero_num = 0, 0
        for s in child_s:
            if s == "1":
                one_num += 1
            else:
                zero_num += 1
        return one_num, zero_num


if __name__ == '__main__':
    print(Solution().findMaxForm(["10", "0", "1"], 1, 1))
