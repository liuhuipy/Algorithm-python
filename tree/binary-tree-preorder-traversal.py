"""
二叉树的前序遍历：
    给定一个二叉树，返回它的前序遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

方法1：
    DFS
方法2：
    BFS
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversql(self, root: TreeNode) -> List[int]:
        res, queue = [], [root]
        while queue:
            node = queue.pop()
            res.append(node.val)
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
        return res

    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node: TreeNode) -> None:
        if not node:
            return
        self.res.append(node.val)
        self.helper(node.left)
        self.helper(node.right)
