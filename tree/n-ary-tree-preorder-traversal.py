"""
N叉树的前序遍历：
    给定一个 N 叉树，返回其节点值的前序遍历。
    例如，给定一个 3叉树 :
    返回其前序遍历: [1,3,5,6,2,4]。

说明: 递归法很简单，你可以使用迭代法完成此题吗?

方法1：
    dfs
方法2：
    bfs
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        deque = [root]
        res = []
        while deque:
            node = deque.pop()
            res.append(node.val)
            for child in node.children[::-1]:
                deque.append(child)
        return res
