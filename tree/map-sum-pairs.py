"""
键值映射：
    实现一个 MapSum 类里的两个方法，insert 和 sum。
    对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。
    对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

示例 1:
    输入: insert("apple", 3), 输出: Null
    输入: sum("ap"), 输出: 3
    输入: insert("app", 2), 输出: Null
    输入: sum("ap"), 输出: 5
"""
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.sum = 0
        self.is_word = False
        self.children = defaultdict(TrieNode)


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        current = self.root
        for s in key:
            current = current.children[s]
            current.sum += val
        if current.is_word:
            for s in key:
                current = current.children[s]
                current.sum = val
        current.is_word = True

    def sum(self, prefix: str) -> int:
        current = self.root
        for s in prefix:
            if not current.children.get(s):
                return 0
            current = current.children[s]
        return current.sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
