"""
二叉树的中序遍历：
    给定一个二叉树，返回它的中序遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

方法1：
    递归
方法2：
    迭代
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, queue, node = [], [], root
        while queue or node:
            if node:
                queue.append(node)
                node = node.left
            else:
                temp = queue.pop()
                res.append(temp.val)
                node = temp.right
        return res

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node: TreeNode) -> None:
        if not node:
            return
        self.helper(node.left)
        self.res.append(node.val)
        self.helper(node.right)
