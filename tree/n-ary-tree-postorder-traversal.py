"""
N叉树的后序遍历：
    给定一个 N 叉树，返回其节点值的后序遍历。
    例如，给定一个 3叉树 :
    返回其后序遍历: [5,6,3,2,4,1].

说明: 递归法很简单，你可以使用迭代法完成此题吗?

方法1：
    dfs
方法2：
    bfs：按根-右-左出队列添加到结果数组里，然后反转结果数组即是后序遍历结果。
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder_dfs(self, root: Node) -> List[int]:
        res = []

        def dfs(node: Node):
            if not node:
                return
            if node.children is not None and isinstance(node.children, list):
                for child in node.children:
                    dfs(child)
            res.append(node.val)

        dfs(root)
        return res

    def postorder_bfs(self, root: Node) -> List[int]:
        if not root:
            return []
        deque = [root]
        temp_res = []
        while deque:
            node = deque.pop()
            temp_res.append(node.val)
            for child in node.children:
                deque.append(child)
        return temp_res[::-1]