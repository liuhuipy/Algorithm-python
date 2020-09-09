"""
最长数对链：
    给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
    现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
    给定一个对数集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

示例 :
    输入: [[1,2], [2,3], [3,4]]
    输出: 2
    解释: 最长的数对链是 [1,2] -> [3,4]
注意：
    给出数对的个数在 [1, 1000] 范围内。

方法：
    动态规划。
    时间复杂度为O(n * n)。空间复杂度为O(n)。
"""
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0
        pairs.sort(key=lambda x: x[1])
        len_pairs = len(pairs)
        dp = [1] * len_pairs
        for i in range(1, len_pairs):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# if __name__ == '__main__':
#     print(Solution().findLongestChain([[7, 9], [4, 5], [7, 9], [-7, -1], [0, 10], [3, 10], [3, 6], [2, 3]]))
