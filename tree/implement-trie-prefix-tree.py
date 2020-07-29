"""
实现Trie（前缀树）：
    实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true

说明:
    你可以假设所有的输入都是由小写字母 a-z 构成的。
    保证所有输入均为非空字符串。

"""
from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for s in word:
            current = current.children[s]
        current.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for s in word:
            if not current.children.get(s):
                return False
            current = current.children[s]
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for s in prefix:
            if not current.children.get(s):
                return False
            current = current.children[s]
        return True


class TreeNode:

    def __init__(self, s):
        self.val = s
        self.next = []


class Trie1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trim = TreeNode("0")
        self.trim.next.append(TreeNode(""))

    @staticmethod
    def find(temp_nodes, word: str) -> (bool, List[TreeNode]):
        for s in word:
            has_node, temp = False, []
            for node in temp_nodes:
                if node.val == s:
                    has_node, temp = True, node.next
                    break
            if not has_node:
                return False, []
            temp_nodes = temp
        return True, temp_nodes

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pre_node = self.trim
        for s in word:
            temp, temp_nodes = None, pre_node.next
            for node in temp_nodes:
                if s == node.val:
                    temp = node
                    break
            if temp is not None:
                pre_node = temp
            else:
                new_node = TreeNode(s)
                pre_node.next.append(new_node)
                pre_node = new_node
        pre_node.next.append(TreeNode(""))

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp_nodes = self.trim.next
        status, nodes = self.find(temp_nodes, word)
        if not status:
            return False
        for node in nodes:
            if node.val == "":
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp_nodes = self.trim.next
        status, nodes = self.find(temp_nodes, prefix)
        return status


# if __name__ == '__main__':
#     trie = Trie()
#     print(trie.insert("apple"))
#     print(trie.search("apple"))
#     print(trie.search("applee"))
#     print(trie.search("app"))
#     print(trie.startsWith("app"))
#     print(trie.insert("app"))
#     print(trie.search("app"))
#     print(trie.insert("app"))
#     print(trie.startsWith("app"))
