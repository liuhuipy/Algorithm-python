"""
两个字符串的删除操作：
    给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
示例：
    输入: "sea", "eat"
    输出: 2
    解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
提示：
    给定单词的长度不超过500。
    给定单词中的字符只含有小写字母。

方法1：
    动态规划：二维数组
    时间复杂度为O(m * n)。空间复杂度为O(m * n)。
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1, len_word2 = len(word1), len(word2)
        if not word1:
            return len_word2
        if not word2:
            return len_word1
        dp = [[0 for _ in range(len_word2 + 1)] for _ in range(len_word1 + 1)]
        for i in range(1, len_word1 + 1):
            dp[i][0] = i
        for j in range(1, len_word2 + 1):
            dp[0][j] = j

        for i in range(1, len_word1 + 1):
            for j in range(1, len_word2 + 1):
                if word1[i - 1] != word2[j - 1]:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1] + 1)
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().minDistance("a", "ate"))
