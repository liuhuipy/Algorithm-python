"""
左叶子之和：
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.left_sum = 0
        self.computeLeftSum(root, "right")
        return self.left_sum

    def computeLeftSum(self, node: TreeNode, temp: str):
        if not node:
            return
        if temp == "left" and not node.left and not node.right:
            self.left_sum += node.val
        self.computeLeftSum(node.left, "left")
        self.computeLeftSum(node.right, "right")
