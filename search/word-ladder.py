"""
单词接龙：
    给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。
    说明:
        如果不存在这样的转换序列，返回 0。
        所有单词具有相同的长度。
        所有单词只由小写字母组成。
        字典中不存在重复的单词。
        你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:
输入:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
输出: 5
解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:
输入:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
输出: 0
    解释: endWord "cog" 不在字典中，所以无法进行转换。

方法1：
    广度优先搜索。
    时间复杂度为：O(M * N)，其中M是单词的长度，N是单词表中单词的总数。
    空间复杂度为：O(M * N)，要在temp_dict字典中记录每个单词的M个通用状态。访问数组的大小是N。
方法2：
    双向广度优先搜索。
"""
from typing import List
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        temp_len = len(beginWord)
        temp_dict = defaultdict(list)
        for word in wordList:
            for i in range(temp_len):
                temp_dict[word[:i] + "*" + word[i + 1:]].append(word)

        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            current_word, temp_level = queue.pop(0)
            for i in range(temp_len):
                temp_word = current_word[:i] + "*" + current_word[i + 1:]
                for word in temp_dict[temp_word]:
                    if word == endWord:
                        return temp_level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, temp_level + 1))
                temp_dict[temp_word] = []
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def visit_word(begin: bool) -> int:
            current_word, level = begin_queue.pop(0) if begin else end_queue.pop(0)
            for i in range(temp_len):
                temp_word = current_word[:i] + "*" + current_word[i + 1:]
                for v_word in temp_dict[temp_word]:
                    if begin:
                        if v_word in end_visited:
                            return level + end_visited[v_word]
                        if v_word not in begin_visited:
                            begin_visited[v_word] = level + 1
                            begin_queue.append((v_word, level + 1))
                    else:
                        if v_word in begin_visited:
                            return level + begin_visited[v_word]
                        if v_word not in end_visited:
                            end_visited[v_word] = level + 1
                            end_queue.append((v_word, level + 1))
            return -1

        temp_len = len(beginWord)
        temp_dict = defaultdict(list)
        for word in wordList:
            for i in range(temp_len):
                temp_dict[word[:i] + "*" + word[i + 1:]].append(word)

        begin_queue = [(beginWord, 1)]
        end_queue = [(endWord, 1)]
        begin_visited = {beginWord: 1}
        end_visited = {endWord: 1}
        while begin_queue and end_queue:
            ans = visit_word(begin=True)
            if ans > 0:
                return ans
            ans = visit_word(begin=False)
            if ans > 0:
                return ans
        return 0


# if __name__ == '__main__':
#     print(Solution().ladderLength2("hit", "cog", ["hot","dot","dog","lot","log"]))
