"""
单词接龙II：
    给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
    每次转换只能改变一个字母。
    转换后得到的单词必须是字典中的单词。
说明:
    如果不存在这样的转换序列，返回一个空列表。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:
    输入:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    输出:
    [
        ["hit","hot","dot","dog","cog"],
        ["hit","hot","lot","log","cog"]
    ]
示例 2:
    输入:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

方法：
    深度优先搜索
"""
from typing import List
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        n = len(beginWord)
        dic = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                dic[word[:i] + "*" + word[i + 1:]].append(word)

        deque = [(beginWord, [beginWord])]
        res = []
        visited = {beginWord}
        while deque:
            temp = []
            temp_visited = set()
            while deque:
                temp_word, local_visit = deque.pop()
                if temp_word == endWord:
                    res.append(local_visit)
                for i in range(n):
                    word = temp_word[:i] + "*" + temp_word[i + 1:]
                    for next_word in dic[word]:
                        if next_word not in visited and next_word not in local_visit:
                            temp.append((next_word, local_visit + [next_word]))
                            temp_visited.add(next_word)
            for visit in temp_visited:
                visited.add(visit)
            deque = temp

        return res


if __name__ == '__main__':
    print(Solution().findLadders("lost",
                                 "cost",
                                 ["most","fist","lost","cost","fish"]))
